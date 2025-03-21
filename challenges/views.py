from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = "January is the first month of the year."
    elif month == 'february':
        challenge_text = "February is the second month of the year."
    elif month == 'march':
        challenge_text = "March is the third month of the year."
    elif month == 'april':
        challenge_text = "April is the fourth month of the year."
    elif month == 'may':
        challenge_text = "May is the fifth month of the year."
    return HttpResponse(challenge_text)