from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

# def index(request):
#     return HttpResponse('Hello World')

monthly_challenges = {
    'January': 'Learn a new language',
    'February': 'Read a book',
    'March': 'Go for a run',
    'April': 'Write a blog post',
    'May': 'Try a new recipe',
    'June': 'Take a photography class',
    'July': 'Volunteer for a local charity',
    'August': 'Go hiking',
    'September': 'Learn a new instrument',
    'October': 'Start a new hobby',
    'November': 'Practice mindfulness',
    'December': 'Reflect on the year'
}

def monthly_challenge(request, month):
    try:
        # Normalize the month parameter to match dictionary keys (capitalized)
        challenge_text = monthly_challenges[month.capitalize()]
        return HttpResponse(challenge_text)
    except KeyError:
        return HttpResponseNotFound('Invalid month')
    
def monthly_challenge_by_number(request, month):
    try:
        # Convert month to an integer
        month = int(month)
        months = list(monthly_challenges.keys())
        if month < 1 or month > len(months):
            return HttpResponseNotFound('Invalid month')
        redirect_month_name = months[month - 1]
        challenge_text = monthly_challenges[redirect_month_name]
        return HttpResponse(challenge_text)
    except ValueError:
        return HttpResponseNotFound('Invalid month')
