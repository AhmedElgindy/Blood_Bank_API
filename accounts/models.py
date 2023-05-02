from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from rest_framework.authtoken.models import Token
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, Fname, DateOfBirth, phone_num,location,blood_group, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not password:
            raise ValueError('password field must be set ')  
        if not Fname:
            raise ValueError('First Name field must be set ')  
        if not DateOfBirth:
            raise ValueError('Date of Birth field must be set ')  
        if not phone_num:
            raise ValueError('Phone number field must be set ')  
        if not location:
            raise ValueError('Location field must be set ')  
        if not blood_group:
            raise ValueError('Blood group field must be set ')  
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, Fname=Fname, DateOfBirth=DateOfBirth, phone_num= phone_num,location = location,blood_group = blood_group ,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, phone_num, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have iis_superuser =True.')
        user = self.model(phone_num = phone_num,**extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        Token.objects.create(user=user)
        return user

class CustomUser(AbstractBaseUser,PermissionsMixin):
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
    Fname = models.CharField(max_length=50, null=True)
    DateOfBirth = models.DateField(null=True)
    password = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=45, unique=True,null=True)
    phone_num = models.CharField(max_length=45, unique=True,null=True)
    location = models.CharField(null=True,max_length=45)
    blood_group = models.CharField(choices=BLOOD_GROUP, max_length=3,null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'phone_num'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()