from django.db import models
from accounts.models import CustomUser

# Create your models here.
class BloodRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blood_requests')
    Fname = models.CharField(max_length=255,)
    location = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add= True)
