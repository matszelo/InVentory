from django.shortcuts import render

# Strona główna aplikacji

def welcome(request):
    return render(request, 'introduce/welcome.html', {})
