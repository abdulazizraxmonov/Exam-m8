from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import Group, Permission
from django.db import models
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    organization = models.CharField(max_length=100)
    login = models.CharField(max_length=60)
    Scienfig_degree = models.CharField(max_length=255)
    Another_information = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='user_photos/', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth']

    objects = CustomUserManager()  

    groups = models.ManyToManyField(Group, verbose_name='groups', related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        related_name='customuser_set',
        blank=True,
    )

    def __str__(self):
        return self.email


    
class EmailVerificationToken(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='verification_token')
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)