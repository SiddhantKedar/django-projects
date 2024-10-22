from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import TODOO
from django.contrib.auth import authenticate, login, logout

def signup(request):
    if request.method == 'POST':
        fnm = request.POST.get("fnm")
        emailid = request.POST.get('email')
        pwd = request.POST.get('pwd')
        print(fnm, emailid, pwd)

        #store in django user
        my_user = User.objects.create_user(fnm, emailid, pwd)
        my_user.save()
        return redirect('/login')
    return render(request, 'signup.html')

def loginn(request):
    if request.method == "POST":
        fnm = request.POST.get('username')
        pwd = request.POST.get('password')
        print(fnm, pwd)
        userr = authenticate(request, username=fnm, password=pwd)
        if userr is not None:
            login(request,userr)
            return redirect('/todo')
        else:
            return redirect('/login')

    return render(request, 'login.html')


def todo(request):
    if request.method == "POST":
        title = request.POST.get('title')
        print(title)
        obj = models.TODOO(title=title, user=request.user)
        obj.save()
        res = models.TODOO.objects.filter(user=request.user).order_by('-data')
        return redirect('/todo', {'res':res})
    res = models.TODOO.objects.filter(user=request.user).order_by('-data')
    return render(request, 'todo.html', {'res':res})
