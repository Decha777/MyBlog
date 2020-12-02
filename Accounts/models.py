from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Skill(models.Model):
     skill_name = models.CharField(max_length=256)
     skill_value = models.IntegerField(default=0)

     def __str__(self):
         return self.skill_name
    
class Experience(models.Model):
     experience_name = models.CharField(max_length=256)
     decription = models.TextField(blank=True)
     start_date = models.DateTimeField(default = timezone.now)
     end_date = models.DateTimeField(default = timezone.now)

     def __str__(self):
         return self.experience_name

class Work(models.Model):
     work_name = models.CharField(max_length=256)
     decription = models.TextField(blank=True)
     link = models.URLField(blank=True)

     def __str__(self):
         return self.work_name


class UserProfileInfo(models.Model):
    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    # Add any additional attributes you want
    birth_date = models.DateTimeField(default = timezone.now)
    job = models.CharField(max_length=256, null=True)
    skills =models.ForeignKey(Skill, on_delete = models.CASCADE,null=True)
    exprerience =models.ForeignKey(Experience, on_delete = models.CASCADE,null=True)
    works =models.ForeignKey(Work, on_delete = models.CASCADE,null=True)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='Images/Proifle',default='Images/None/avatar.png', max_length=None)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('Accounts:profile', kwargs ={'pk':self.pk})