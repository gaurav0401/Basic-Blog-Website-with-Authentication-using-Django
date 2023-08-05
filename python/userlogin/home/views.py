from django.shortcuts import render , redirect

#use -  admin1
#passwd-  Ab22558800

# from django.contrib.auth.models import User
from django.contrib.auth import logout  , authenticate , login

# Create your views here.


def index (request):
    if request.user.is_anonymous:
        return render(request , 'login.html')

    return render(request , 'index.html')


def login_user(request):
    if request.method=="POST":
        username=request.POST.get('username')
        passwd=request.POST.get('password')

        user=authenticate(username=username , password=passwd)
        if user is not None:
            login(request , user)
            return redirect('/')
        else:
             return render(request ,  'login.html')
    return render(request ,  'login.html')

def logout_user(request):

    logout(request )

    return redirect('/login')


