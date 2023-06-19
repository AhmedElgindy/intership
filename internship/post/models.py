from django.db import models
from user.models import UserProfile
from django import forms
 
class Post(models.Model):
    doctor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    summary = models.CharField(max_length=200)
    content = models.TextField()
    CATEGORY_CHOICES = [
        ('mental_health', 'Mental Health'),
        ('heart_disease', 'Heart Disease'),
        ('covid19', 'COVID-19'),
        ('immunization', 'Immunization'),
    ]
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'category', 'summary', 'content']