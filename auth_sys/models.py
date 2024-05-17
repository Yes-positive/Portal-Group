from django.contrib.auth.models import User
from django.db import models

class UserPortal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username + '-' + self.role