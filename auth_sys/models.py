from django.contrib.auth.models import User, AbstractUser
from django.db import models

class UserPortal(AbstractUser):
   USER_ROLES = (
       ('studentPortal', 'Учень'),
       ('teacherPortal', 'Вчитель'),
       ('moderatorPortal', 'Модератор'),
   )
   role = models.CharField(max_length=15, choices=USER_ROLES, default='student')
    

class StudentPortal(models.Model):
    user = models.OneToOneField(UserPortal, on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ("view_student", "Can view student"),
           )


class TeacherPortal(models.Model):
    user = models.OneToOneField(UserPortal, on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ("view_teacher", "Can view teacher"),
            ("edit_course", "Can edit course"),
           )

class ModeratorPortal(models.Model):
    user = models.OneToOneField(UserPortal, on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ("view_moderator", "Can view moderator"),
            ("edit_user", "Can edit user"),
            ("ban_user", "Can ban user")
          )