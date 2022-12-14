from django.shortcuts import render

def welcome(request):
    return render(request, 'introduce/welcome.html', {})
