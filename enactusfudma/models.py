from django.db import models
import random


class AlumniProfile(models.Model):
    def imageUploadPath(instance, filename):
        randomNumber = (random.randint(1,100000000))
        return ''.join(['alumniProfilePicture/', str(randomNumber) + filename])

    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    profilePicture = models.ImageField(null=True, upload_to=imageUploadPath, blank=True)
    phone = models.CharField(max_length=255,null=True, blank=True)
    address = models.CharField(max_length=255,null=True, blank=True)
    about = models.CharField(max_length=255,null=True, blank=True)
    
    def __str__(self):
        return str(self.first_name)


class ActiveStudentProfile(models.Model):
    def imageUploadPath(instance, filename):
        randomNumber = (random.randint(1,100000000))
        return ''.join(['activeStudentProfilePicture/', str(randomNumber) + filename])

    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    profilePicture = models.ImageField(null=True, upload_to=imageUploadPath, blank=True)
    phone = models.CharField(max_length=255,null=True, blank=True)
    address = models.CharField(max_length=255,null=True, blank=True)
    about = models.CharField(max_length=255,null=True, blank=True)
    
    def __str__(self):
        return str(self.first_name)
