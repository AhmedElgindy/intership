from django.db import models
from django.contrib.auth.models import AbstractUser
class UserProfile(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='images')
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    address_line1 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)

    REQUIRED_FIELDS = []
    def __str__(self):
        return self.username

