from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from .forms import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group



def home_view(request):
    return render(request, 'hospital/index.html')


def adminclick_view(request):
    return render(request, 'hospital/adminclick.html')

def doctorclick_view(request):
    return render(request, 'hospital/doctorclick.html')

def patient_click_view(request):
    return render(request, 'hospital/patientclick.html')

def admin_signup_view(request):
    return render(request, 'hospital/adminsignup.html')

def doctor_signup_view(request):
    return render(request, 'hospital/doctorsignup.html')

def patient_signup_view(request):
    return render(request, 'hospital/patientsignup.html')



def admin_signup_view(request):
    form=forms.AdminSigupForm()
    if request.method=='POST':
        form=forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            return HttpResponseRedirect('adminlogin')
    return render(request,'hospital/adminsignup.html',{'form':form})



# Create your views here.


