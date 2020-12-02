from django.db import models
from django.utils import  timezone
from django.urls import  reverse
from ckeditor.fields import  RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=256, default='Programming')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:index')

class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null=True)
    title = models.CharField(max_length=256)
    post_pic = models.ImageField(upload_to='Images/header/',default='Images/header/blog_defualt.jpg', max_length=None)
    content = RichTextField(blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_published = models.DateTimeField(blank = True, null=True)


    def publish(self):
        self.date_published = timezone.now()
        self.save()
    
    def approve_comments(self):
        return self.comments.filter(approved_comments = True)
    

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs ={'pk':self.pk})
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post',  related_name = 'comments', on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    text = RichTextField(blank=True, null=True)
    date_created = models.DateTimeField(default = timezone.now)
    approved_comments = models.BooleanField( default = False)


    def approve(self):
        self.approved_comments = True
        self.save()

    def get_absolute_url(self):
        return reverse('blog:post_list')

    def __str__(self):
        return self.text