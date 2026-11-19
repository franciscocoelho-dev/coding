from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.messages import constants
from django.contrib import messages

def registrar(request):
    if request.method == 'POST':    
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso.')
            return redirect('/account/login/')
    else:
        user_form = UserCreationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

def acessar(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/sistema/home')
    else:
        form_authenticate = AuthenticationForm()

    return render(request, 'account/login.html', {'form_authenticate': form_authenticate})


def sair(request):
    logout(request)
    return redirect('/account/login')








