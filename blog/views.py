from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import AddPostForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth import  authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Post
# Create your views here.

@login_required(login_url = 'login')
def home(request):
    context = {}
    return render(request, 'home.html', context)

def loginView(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
           messages.info(request,"Invalid Username or Password")
    context={
      
    }
    return render(request,'login.html',context)

@login_required(login_url = 'login')
def logoutView(request):
    logout(request)
    return redirect('login')


def register(request):
    register_form = CreateUserForm()
    if request.method == "POST":
        register_form = CreateUserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('login')
            
    context={
        "register_form" : register_form 
    }
    return render(request,'register.html',context)

@login_required(login_url = 'login')
def addPost(request):
    post_form = AddPostForm()
    if request.method == "POST":
        post_form = AddPostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts')
    context={"post_form" : post_form }
    return render(request,"newpost.html", context)

def postList(request):
    posts = Post.objects.all()
    context={"posts" : posts}
    return render(request,'posts.html', context)

@login_required(login_url = 'login')
def postDetail(request,id):
    post = Post.objects.get(id=id)
    context={"post" : post}
    return render(request,'post_detail.html', context)
