from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    INST_CHOICES = (
        ('vocal', 'vocal'),
        ('drum', 'drum'),
        ('elec', 'elec'),
        ('piano', 'piano'),
        ('bass', 'bass'),
        ('other', 'other'),
    )
    
    inst = models.CharField(max_length=20, choices=INST_CHOICES)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField()
    file = models.FileField(upload_to="music", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
class Jam(models.Model):
    INST_CHOICES = (
        ('vocal', 'vocal'),
        ('drum', 'drum'),
        ('elec', 'elec'),
        ('piano', 'piano'),
        ('bass', 'bass'),
        ('other', 'other'),
    )
    inst = models.CharField(max_length=20, choices=INST_CHOICES)
    project = models.ForeignKey(Project, on_delete = models.CASCADE, related_name='jams')
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField()
    file = models.FileField(upload_to="music", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    