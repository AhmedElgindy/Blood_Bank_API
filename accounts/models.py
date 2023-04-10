from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, Fname, Lname, DateOfBirth, state, city, street, sex, phone_num, salary, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not password:
            raise ValueError('password field must be set ')  
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, Fname=Fname, Lname=Lname, DateOfBirth=DateOfBirth, state=state, city=city, street=street, sex=sex, phone_num=phone_num, salary=salary, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have iis_superuser =True.')
        user = self.model(email = email,**extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
class CustomUser(AbstractBaseUser,PermissionsMixin):
    Fname = models.CharField(max_length=20, null=True)
    Lname = models.CharField(max_length=20, null=True)
    DateOfBirth = models.DateField(null=True)
    state = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=20, null=True)
    street = models.CharField(max_length=30, null=True)
    sex = models.CharField(max_length=6, null=True)
    password = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=45, unique=True)
    phone_num = models.CharField(max_length=45, null=True)
    salary = models.CharField(max_length=45, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()