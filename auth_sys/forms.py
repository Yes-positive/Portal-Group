from django import forms
from .models import UserPortal

class RoleFormPortal(forms.ModelForm):
    class Meta:
        model = UserPortal
        fields = ['role']
        labels = {
            'role': 'Оберить роль',
        }