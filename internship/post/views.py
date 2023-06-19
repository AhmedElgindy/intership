from django.shortcuts import render,redirect
from .models import PostForm
# Create your views here.

def create(request):
    if not request.user.is_authenticated or not request.user.is_doctor:
        return redirect('login') 
    form = PostForm(request.POST,request.FILES) # request.FILES to handle the image in the form 
    if form.is_valid():
        post = form.save(commit=False)
        post.doctor = request.user 
        form.save()
        return render(request,"createBlog.html")
    else:
        print(form.errors)
    return render(request,"createBlog.html")