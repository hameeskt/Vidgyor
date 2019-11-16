from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render, redirect



# Create your models here.


class Tags(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Video(models.Model):
    VIDEO_STATUS = (('ready', 'Ready'), ('inactive', 'Inactive'))
    video_file = models.FileField(upload_to='videos')
    title = models.CharField(max_length=50)
    desc = models.TextField()
    tag = models.ManyToManyField(Tags)
    thumb = models.ImageField(upload_to='pics')
    type = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,choices=VIDEO_STATUS, default='ready')
    duration = models.FloatField(default=0.0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    uploaded_by = models.CharField(max_length=30, default=User,)

    def __str__(self):
        return self.title


class VideoViews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video,on_delete=models.CASCADE)

    def __str__(self):
        return self.user
