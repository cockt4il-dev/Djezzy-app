from django.shortcuts import render,redirect #N
from django.http import HttpResponse 
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.contrib.auth import authenticate, login #N
from django.contrib import messages #N
from .models import NPSQuestions, NPSResponses, MonthlyResponseCounts  # Import your model
from django.db.models import Count  # Import Count for aggregation
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt
from django.db.models.functions import TruncMonth, Cast
from django.db.models import Count, DateTimeField
from django.http import JsonResponse
from django.core.cache import cache
from .models import NPSResponses  
from django.db.models import F


from django.core.paginator import Paginator

def home_redirect(request):
    if request.user.is_authenticated:
        return redirect("dashboard")  
    return redirect("login")  

# Create your views here.
def dashboard(request):
    
    return render(request, 'dashboard.html')

def predictions(request):
    
    return render(request, 'predictions.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return JsonResponse({'error': 'Both fields are required'}, status=400)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Logs in the user
            return redirect('dashboard') 
            
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)

    return render(request, 'login.html')  # Render HTML login form



def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username or not email or not password:
            return JsonResponse({'error': 'All fields are required'}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already taken'}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)

        return JsonResponse({'message': 'User registered successfully'}, status=201)

    return render(request, 'signup.html')  # Render HTML signup form for GET requests


@csrf_exempt
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")
    return redirect("login")



@login_required
def get_chart_data(request):
    print("User:", request.user)
    try:
        data = (
            NPSQuestions.objects.values('survey_type__survey_name')
            .annotate(count=Count('survey_type'))
        )

        labels = [entry['survey_type__survey_name'] for entry in data]  # Get survey names
        counts = [entry['count'] for entry in data]

        return JsonResponse({'labels': labels, 'data': counts})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    

def get_lang_chart_data(request):
    try:
        data = (
            NPSQuestions.objects.values('lang_id')
            .annotate(count=Count('lang_id'))
        )

        labels = [entry['lang_id'] for entry in data]  # Get survey names
        counts = [entry['count'] for entry in data]

        return JsonResponse({'labels': labels, 'data': counts})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    

    
def questions(request):
    all_data = NPSQuestions.objects.all().order_by('id')  # Ensure ordering
    paginator = Paginator(all_data, 6)  # Show 10 items per page

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    total_questions = NPSQuestions.objects.count()
    

    # Fetch unique lang_id values from the database
    unique_lang_ids = NPSQuestions.objects.values_list('lang_id', flat=True).distinct()
    unique_question_types = NPSQuestions.objects.values_list('question_type', flat=True).distinct()

    context = {
        'page_obj': page_obj,
        'total_questions': total_questions,  # Pass total surveys to template
        'lang_ids': unique_lang_ids,
        'question_types' : unique_question_types,
    }

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':  # AJAX request
        data = list(page_obj.object_list.values('id', 'survey_type_id','lang_id','question_number','regexp_replace','question_name','question_type' ))  # Explicitly get survey_type_id
        return JsonResponse({'data': data, 'has_next': page_obj.has_next()})

    return render(request, 'questions.html', context)



def filtered_data(request):
    lang_id = request.GET.get('lang_id', '')
    question_type = request.GET.get('question_type', '')

    # Filter the database based on selected values
    queryset = NPSQuestions.objects.all()
    if lang_id:
        queryset = queryset.filter(lang_id=lang_id)
    if question_type:
        queryset = queryset.filter(question_type=question_type)

    # Convert queryset to JSON response
    data = list(queryset.values('id', 'survey_type_id', 'lang_id', 'question_number', 'regexp_replace', 'question_name', 'question_type'))
    return JsonResponse({"data": data})

def search_data(request):
    query = request.GET.get('query', '')

    # Search in the "regexp_replace" column
    queryset = NPSQuestions.objects.filter(regexp_replace__icontains=query) if query else NPSQuestions.objects.all()

    # Convert queryset to JSON
    data = list(queryset.values('id', 'survey_type_id', 'lang_id', 'question_number', 'regexp_replace', 'question_name', 'question_type'))
    return JsonResponse({"data": data})

def format_number(num):
    """Convert a large number into a human-readable format using K, M, B, T."""
    if num >= 1_000_000_000_000:
        return f"{num / 1_000_000_000_000:.2f}T"
    elif num >= 1_000_000_000:
        return f"{num / 1_000_000_000:.2f}B"
    elif num >= 1_000_000:
        return f"{num / 1_000_000:.2f}M"
    elif num >= 1_000:
        return f"{num / 1_000:.2f}K"
    else:
        return str(num)


# Estimated total count value (optimized)
def analytics(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT reltuples::bigint FROM pg_class WHERE relname = 'calc_npsresponses';")
        total_responses = cursor.fetchone()[0]  # Estimated count

    context = {'total_responses': format_number(int(total_responses))}
    
    return render(request, 'analytics.html', context)


def monthly_data(request):
    data = MonthlyResponseCounts.objects.all().order_by("year_month")
    labels = [entry.year_month for entry in data]
    counts = [entry.count for entry in data]

    return JsonResponse({"labels": labels, "data": counts})



from django.http import JsonResponse
from django.utils.timezone import now
from django.db import connection

def refresh_materialized_view(request):
    # Get the current date
    current_date = now().date()

    # Check if it's the first day of the month
    if current_date.day == 1:
        with connection.cursor() as cursor:
            cursor.execute("REFRESH MATERIALIZED VIEW monthly_response_counts;")

        return JsonResponse({"status": "success", "message": "Materialized view refreshed!"})
    else:
        return JsonResponse({"status": "skipped", "message": "Not the first of the month!"})



def get_question_type_data(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT question_type, response_count FROM question_type_summary;")
        rows = cursor.fetchall()

    data = {
        "labels": [row[0] for row in rows],  
        "counts": [row[1] for row in rows],  
    }
    return JsonResponse(data)



def get_nps_overview_data(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT label, percentage, count FROM nps_overview;")
        rows = cursor.fetchall()

    # Extract data
    labels = [row[0] for row in rows]  # 'Promoters', 'Passives', 'Detractors'
    percentages = {row[0]: row[1] for row in rows}  # {'Promoters': xx, 'Passives': yy, 'Detractors': zz}
    counts = {row[0]: row[2] for row in rows}  # {'Promoters': xx, 'Passives': yy, 'Detractors': zz}

    # Calculate NPS Score: (% Promoters - % Detractors)
    nps_score = round(percentages.get('Promoters', 0) - percentages.get('Detractors', 0))

    data = {
        "labels": labels,
        "percentages": list(percentages.values()),
        "counts": list(counts.values()),
        "nps_score": nps_score  # Include NPS Score in API response
    }

    return JsonResponse(data)

def get_nps_distribution(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT response_parsed, response_count FROM nps_responses_distribution ORDER BY response_parsed ASC;")
        rows = cursor.fetchall()

    # Extract data for Chart.js
    labels = [str(row[0]) for row in rows]  # response_parsed (1,2,3,...,10)
    data = [row[1] for row in rows]         # response_count (values)

    return JsonResponse({'labels': labels, 'data': data})



