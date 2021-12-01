from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .models import Profile
from django.urls import reverse

# Create your views here.
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile': profile})
