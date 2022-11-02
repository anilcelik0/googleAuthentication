from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import photo_share
from .forms import *


# Create your views here.

def index(request):
    if request.method=="POST":
        form = UserImage(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            form = UserImage()
            return render(request, 'index.html', {'form' : form})

    else:
        if request.user.is_authenticated:
            photos=photo_share.objects.filter(user=request.user)
            form = UserImage()
            return render(request, 'index.html', {'form' : form,'photos':photos})
        else:
            return render(request,'index.html')