from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'profils/sign-in.html')

def dashboard(request):
    return render(request, 'profils/dashboard.html')

def profile(request):
    return render(request, 'profils/profile.html')