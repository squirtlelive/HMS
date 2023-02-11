from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings



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

def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()



# Create your views here.


