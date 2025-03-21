from django.urls import path
from . import views
urlpatterns = [
   path('<str:month>',views.monthly_challenge), # <str:month> is a path converter that captures the month from the URL and passes it to the view as a string.
]