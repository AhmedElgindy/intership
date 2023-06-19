from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='blog-create'),
    path('doctor_blogs/', views.doctor_blogs, name='doctor_blogs'),
    path('blogs/',views.display_posts,name = 'blogs'),
]