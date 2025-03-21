from django.urls import path
from . import views


urlpatterns = [
    path('',views.home_redirect, name='home'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path('api/chart-data/', views.get_chart_data, name='chart-data'),
    path('api/lang-chart-data/', views.get_lang_chart_data, name='lang-chart-data'),
    path("questions/", views.questions, name="questions"),
    path('filtered-data/', views.filtered_data, name='filtered_data'),
    path('search-data/', views.search_data, name='search_data'),
    path("predictions/", views.predictions, name="predictions"),
    path("analytics/", views.analytics, name="analytics"),   
    path('api/monthly-data/', views.monthly_data, name='monthly_data'),
    path("refresh-view/", views.refresh_materialized_view, name="refresh_materialized_view"),
    path("api/question-type-data/", views.get_question_type_data, name="question-type-data"),
    path("api/nps-overview-data/", views.get_nps_overview_data, name="question-type-data"),
    path("api/nps-distribution/", views.get_nps_distribution, name="nps-distribution"),
]

