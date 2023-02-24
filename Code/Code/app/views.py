from dataclasses import fields
from urllib import request
from django.shortcuts import render,redirect
from app.forms import CustomUserCreationForm, ReportForm
from app.models import CustomUser,Report
from django.contrib.auth import logout,login,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django_otp.decorators import otp_required
from django.shortcuts import render, get_object_or_404, redirect
from two_factor.views import LoginView
from django.views import View

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.generic.edit import UpdateView
from django.http import HttpResponse, JsonResponse, QueryDict

from rest_framework.views import APIView  
from django.http import JsonResponse  

@login_required
def home_view(request):
    reports = Report.objects.filter(user=request.user)
    
    context = {
        'reports':reports,
    }
    return render(request,'app/home.html',context)

@login_required
def create_report(request):
    form = ReportForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():           
            report = form.save(commit=False)            
            report.user = request.user
            report.save()
            return redirect('home')
            
    context = {
        'form':form,
    }
    return render(request,'app/report-form.html',context)



def register_user(request):
    form = CustomUserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User was created successfully.')
            
            return redirect('login')
           
        else:
            messages.error(request, 'An error has occurred during registration.')
    context = {
        'form':form,
    }
    return render(request,'app/register.html',context)



def login_user(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        try:
            user = CustomUser.objects.get(username=username)
        except:
            messages.error(request, 'Username Does not exist')
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'Successfully logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Username or Password is incorrect.')

class CustomLoginView(LoginView):
    template_name = 'app/customlogin.html'


def logout_user(request):
    logout(request)    
    return redirect('/app/login')


@login_required
def Edit_Report(request, id):
    obj = {}
    if id:
        report = get_object_or_404(Report, pk=id)
    else:
        report = Report()
    user_form = ReportForm(instance=report, prefix='report')

    if request.method == 'POST':
        form = ReportForm(request.POST, instance=report, prefix='report')
        if form.is_valid():
             form.save()
             messages.success(request, "You successfully updated the report")
             return redirect('home')
    else:
        obj['form'] = user_form
        return render(request, 'app/edit-report-form.html', obj)
  
  
  


     