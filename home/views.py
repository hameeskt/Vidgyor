from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .forms import *
from django.http import HttpResponse
from django.views.generic import UpdateView
from django.shortcuts import get_object_or_404
from .filter import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        videos = Video.objects.all()
        count = Video.objects.count()
        video_filter = VideoFilter(request.GET, queryset=videos)




        return render(request, 'main_page.html',{'videos' : videos, 'count': count,'filter': video_filter,})
    else:
        return redirect('login')

# def search(request):
#     video_list = Video.objects.all()
#     video_filter = VideoFilter(request.GET, queryset=video_list)
#     return render(request, 'search.html', {'filter': video_filter})

def reg(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken, try something else :( ')
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken, try something else :( ')
                return redirect('/')
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save()
                messages.info(request,'user created successfully :)')
                return redirect('/')

        else:
            messages.info(request,'password not matching')
            return redirect('/')
    else:
        return render(request, 'reg.html')


def log(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password1']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            # messages.info(request,'success')
            return redirect('/')
        else:
            messages.info(request,'Username or Password Incorrect :(')
            return redirect('login')
    else:
        return render(request,'welcome.html')
    # return render(request,'log.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

# def video_upload(request):
#     return render(request,'video_upload.html')
def add_tag(request):
    if request.method== 'POST':
        tag_form = TagsForm(request.POST, request.FILES)

        if tag_form.is_valid():
            tag_form.save()
            return redirect('video_upload')
    else:
        tag_form = TagsForm()
        return render(request,'add_tag.html', {'tag_form' : tag_form})

def add_category(request):
    if request.method== 'POST':
        form = CategoryForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('video_upload')

    else:
        form = CategoryForm()
        return render(request,'add_category.html', {'form' : form})


def video_upload(request):
    if request.method == 'POST':
        form1 = VideoForm(request.POST, request.FILES)

        if form1.is_valid():
            form1.save()
        return redirect('success')
    else:
        form1 = VideoForm()
    return render(request, 'video_upload.html', {'form1': form1})


def success(request):
    return HttpResponse('successfuly uploaded')

def details(request,id):
    vi= Video.objects.get(id=id)
    video = get_object_or_404(Video, id=id)
    if request.method == "POST":
        form = VideoEditForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = VideoEditForm(instance=video)
    return render(request,'details.html',{'vi':vi, 'form':form})
