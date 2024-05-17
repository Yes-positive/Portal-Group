from django.contrib import admin
from django.urls import path
from .views import CustomLoginView, TemplateView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login-form'),
    path('roles/', TemplateView.as_view(), name='roles-name'),
]
