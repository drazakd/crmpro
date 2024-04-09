from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
@login_required(login_url='home')
def dashboard(request):
    return render(request, 'profils/dashboard.html')

@login_required(login_url='home')
def profile(request):
    return render(request, 'profils/profile.html')