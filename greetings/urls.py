from django.urls import path
from . import views

urlpatterns = [
    path('<int:month>/', views.monthly_challenge_by_number),  # Numeric month
    path('<str:month>/', views.monthly_challenge),            # String month
]