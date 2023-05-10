from django.db import models
from accounts.models import CustomUser

# Create your models here.
class BloodRequest(models.Model):
    BLOOD_GROUP = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blood_requests')
    Fname = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add= True)
    #blood group 
    blood_group = models.CharField(choices=BLOOD_GROUP, max_length=3,null=True)

    approved = models.BooleanField(default=False)


class Donate(models.Model):
        BLOOD_GROUP = [
            ('A+', 'A+'),
            ('A-', 'A-'),
            ('B+', 'B+'),
            ('B-', 'B-'),
            ('O+', 'O+'),
            ('O-', 'O-'),
            ('AB+', 'AB+'),
            ('AB-', 'AB-'),
        ]
        user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='donate')
        Fname = models.CharField(max_length=255)
        location = models.CharField(max_length=255)
        date = models.DateField(auto_now_add=True)
        time = models.TimeField(auto_now_add= True)
        #blood group 
        blood_group = models.CharField(choices=BLOOD_GROUP, max_length=3,null=True)
        approved = models.BooleanField(default=False)
    