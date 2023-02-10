from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home_view(request):
    return render(request, 'hospital/index.html')


def adminclick_view(request):
    return render(request, 'hospital/adminclick.html')

def doctorclick_view(request):
    return render(request, 'hospital/doctorclick.html')

def patient_click_view(request):
    return render(request, 'hospital/patientclick.html')



# Create your views here.


