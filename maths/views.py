from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from .models import Maths
from users.models import Profile
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'maths/home.html')

# @login_required(login_url="/users/login/")
def createmaths(request):
    '''
    function for creating the maths topics
    '''
    current_user=request.user
    instructor = Profile.objects.get(user=current_user)
    user = Profile.objects.get(user=current_user)
    maths = user.math_id
    
    if request.method == 'POST':
        form = MathsForm(request.POST, request.FILES)
        if form.is_valid():
            maths = form.save(commit=False)
            maths.instructor = current_user
            maths.timestamp = timezone.now()
            maths.save()
        return redirect('maths-home')
    else:
        form = MathsForm()

    return render(request, 'maths/math_form.html', {"form":form, "current_user":current_user, "instructor":instructor, "user":user, "maths":maths})

def algebra1(request):
    users = Profile.objects.all()
    current_user=request.user
    maths = Maths.objects.all()
    return render(request, 'maths/algebra.html', {"current_user":current_user, "maths":maths, "users":users})

def about(request):
    return render(request, 'maths/about.html', {'title': 'About'})