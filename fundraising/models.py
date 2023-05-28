from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, Group, Permission
from PIL import Image



class User(AbstractUser):
    mobile_regex = RegexValidator(
        regex=r'^01[0-9]{9}$',
        message="Mobile number must be entered in the format: '01012345678'."
    )
    mobile_phone = models.CharField(validators=[mobile_regex], max_length=11)
    profile_picture = models.ImageField(upload_to='profile_pictures')
    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT, default=1)

    total_target = models.DecimalField(max_digits=10, decimal_places=2)
    pictures = models.ManyToManyField('ProjectPicture', blank=True)
    tags = models.ManyToManyField('Tag', blank=True)

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    def __str__(self):
        return self.title





class ProjectPicture(models.Model):
    image = models.ImageField(upload_to='project_pictures')



class Tag(models.Model):
    name = models.CharField(max_length=50)
    def _str_(self):
            return self.name
    

    

