from django.shortcuts import render,HttpResponse,redirect
from app01 import forms
from django.contrib import auth
from app01.models import UserInfo


def login(request):
    form_obj = forms.RegForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = auth.authenticate(request,username=username,password=password)
        print('obj11',obj)
        if obj:
            auth.login(request,obj)
            next = request.GET.get('next')
            if next:
                return redirect(next)
            return redirect('/index/')

    return render(request,'login.html',{'form_obj':form_obj})


def index(request):
    return render(request,'index.html')


def reg(request):
    form_obj = forms.RegForm()
    if request.method == 'POST':
        form_obj = forms.RegForm(request.POST)
        # username = request.POST.get('username')
        # pwd = request.POST.get('pwd')
        if form_obj.is_valid():
            form_obj.cleaned_data.pop('re_password')
            UserInfo.objects.create_user(**form_obj.cleaned_data)
            return redirect('/login/')
    return render(request,'reg.html',{'form_obj':form_obj})


def logout(request):
    auth.logout(request)
    return redirect('/login/')