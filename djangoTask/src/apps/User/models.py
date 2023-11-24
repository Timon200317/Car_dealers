from django.db import models
from django.contrib.auth.models import AbstractUser
from djangoTask.src.core.enums.enums import UserProfile


class User(AbstractUser):
    user_type = models.CharField(max_length=10,
                                 choices=[(type_user.value, type_user.name) for type_user in UserProfile],
                                 default=UserProfile.NONE.value
                                 )

    def __str__(self):
        return self.username
