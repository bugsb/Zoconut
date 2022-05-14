from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(f'/app/home/all_payments?user={user.id}')
        else:
            messages.success(request,"Invalid Credentials")
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')
