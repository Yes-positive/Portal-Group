from django.contrib import admin
from django.urls import path
from .views import CustomLoginView, ChooseRoleView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login-form'),
    path('roles/',ChooseRoleView.as_view(), name='roles-name'),
]
