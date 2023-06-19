from django.shortcuts import render,redirect
from .models import PostForm,Post
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


def doctor_blogs(request):
    if not request.user.is_authenticated or not request.user.is_doctor:
        return redirect('login')
    
    doctor_posts = Post.objects.filter(doctor=request.user)
    
    return render(request, 'doctor_blogs.html', {'doctor_posts': doctor_posts})

def display_posts(request):
    posts = Post.objects.filter(draft=False)

    context = {
        'posts': posts,
    }
    return render(request, 'blog_list.html', context)