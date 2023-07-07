from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, HttpResponse
from .models import VaccineCenters
from .form import CenterFilter


# # Create your views here.
#
@login_required
def HomePage(request):
    return render(request, 'index.html', {})


def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('sname')
        name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        new_user = User.objects.create_user(name, email, password)
        new_user.first_name = fname
        new_user.last_name = lname

        new_user.save()
        return redirect('login-page')

    return render(request, 'register.html', {})


def Login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            return HttpResponse('Error, user does not exist')

    return render(request, 'login.html', {})


def logoutuser(request):
    logout(request)
    return redirect('login-page')


def search(request):

    context = {'form': CenterFilter(),
               'vaccine': VaccineCenters.objects.all()
               }
    return render(request, 'slot.html', context)
