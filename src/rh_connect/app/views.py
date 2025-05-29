from django.shortcuts import render

# Create your views here.
# suporte/views.py

from django.shortcuts import render, redirect
from django.contrib import messages # Para exibir mensagens de feedback
# from django.contrib.auth.decorators import login_required # Se precisar que o usuário esteja logado

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = "login.html"
