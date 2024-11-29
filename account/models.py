from django.contrib.auth.models import AbstractUser
from django.db import models
from django_resized import ResizedImageField
import uuid

class User(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True, null=False)
    #avatar = models.ResizedImageField(size=[300,300], default='avatar.png')
    date_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username