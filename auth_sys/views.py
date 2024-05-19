from django.views.generic.edit import FormView
from .forms import RoleFormPortal
from django.views import View
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .models import StudentPortal, TeacherPortal, ModeratorPortal


class CustomLoginView(LoginView):
    template_name = 'auth_sys/login.html'


class StudentView(View):
    def get(self, request):
        return render(request, template_name='auth_sys/student_portal.html')
    

class TeacherView(View):
    def get(self, request):
        return render(request, template_name='auth_sys/teacher_portal.html')
    

class ModeratorView(View):
    def get(self, request):
        return render(request, template_name='auth_sys/moder_portlal.html')
    
class ChooseRoleView(FormView):
    template_name = 'auth_sys/roles'
    form_class = RoleFormPortal
    success_url = '/index/'

    def form_valid(self, form):
        form.save()
        return super().form_Valid(form)