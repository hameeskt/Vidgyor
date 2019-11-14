from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'welcome.html')

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
            messages.info(request,'success')
            return render(request,'home.html')
        else:
            messages.info(request,'Username or Password Incorrect :(')
            return redirect('/')
    else:
        return render(request,'log.html')
    # return render(request,'log.html')


def logout(request):
    auth.logout(request)
    return redirect('/')