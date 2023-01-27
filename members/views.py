from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Logowanie użytkownika do aplikacji

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('equipment_list') # Poprawna autoryzacja danych
        else:
            messages.success(request, "Niepoprawne dane logowania, spróbuj ponownie") # Wyświetlenie komunikatu po wpisaniu niepoprawnych danych
            return redirect('login_user')
    else:
        return render(request, 'members/login.html', {}) 

# Wylogowanie użytkownika z aplikacji    
    
def logout_user(request):
    logout(request)
    messages.success(request, "Zostałeś poprawnie wylogowany") # Komuniakt o poprawnym wylogowaniu
    return redirect('welcome')

