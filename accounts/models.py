from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import random
# Create your models here.

class userManager(BaseUserManager):
    def create_user(self, email, regCode, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Users must have email address")
        if not password:
            raise ValueError("Users must have password")
        user_obj = self.model(email = self.normalize_email(email),regCode=regCode)
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.is_active = is_active
        user_obj.admin = is_admin
        user_obj.save(using=self._db)
        return user_obj
    def create_staffuser(self, email, regCode, password=None):
        user = self.create_user(
            email,
            regCode,
            password=password,
            is_staff=True
        )   
        return user 
    def create_superuser(self, email, regCode, password=None):
        user = self.create_user(
            email,
            regCode,
            password=password,
            is_staff=True,
            is_admin=True
        )   
        return user 

class User(AbstractBaseUser):
    email   = models.EmailField(max_length=255, unique=True)
    staff  = models.BooleanField(default=False)
    admin  = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    reg_date = models.DateTimeField(auto_now_add=True)
    regCode = models.CharField(max_length=255, default='enactusfudma')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['regCode']
    objects = userManager()

    def __str__(self):
        return self.email
    def get_short_name(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True  

    
    @property
    def is_staff(self):
        return self.staff
    @property
    def is_admin(self):
        return self.admin
  


class Profile (models.Model):
    def imageUploadPath(instance, filename):
        randomNumber = (random.randint(1,100000000))
        return ''.join(['userProfilePicture/', str(randomNumber) + filename])

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    firstName = models.CharField(max_length=255, null=True, blank=True)
    lastName = models.CharField(max_length=255, null=True, blank=True)
    profilePicture = models.ImageField(null=True, upload_to=imageUploadPath, blank=True)

    def __str__(self):
        return str(self.firstName)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print("user profile created")

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()
        print('user profile updated')

    