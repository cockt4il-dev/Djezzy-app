from django.urls import path
from . import views


urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path('api/chart-data/', views.get_chart_data, name='chart-data'),
    path('api/lang-chart-data/', views.get_lang_chart_data, name='lang-chart-data'),
    path("questions/", views.questions, name="questions"),
    path('filtered-data/', views.filtered_data, name='filtered_data'),
    path('search-data/', views.search_data, name='search_data'),
    path("predictions/", views.predictions, name="predictions"),
    path("analytics/", views.analytics, name="analytics"),   
]

