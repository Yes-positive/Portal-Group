from typing import Any
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView 


class CustomLoginView(LoginView):
    template_name = 'auth_sys/login.html'


class TemplateView(TemplateView):
    template_name = 'auth_sys/roles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
