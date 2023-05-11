from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import *

#menu = ["Login", "Registration", "Data", "About"]

menu = [{'title': "Data", 'url_name': 'data'},
        {'title': "About", 'url_name': 'about'},
        {'title': "Login", 'url_name': 'login'},
        {'title': "Registration", 'url_name': 'reg'}]



def home(request):
    return render(request, 'site/home.html', {'title':'home', 'menu':menu})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
    #return redirect('/', permanent=True)


class SignUpGeneral(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'site/signup.html'

class SignUpHR(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('site/registration/login')
    template_name = 'site/signup_hr.html'

class SignUpPM(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('site/registration/login')
    template_name = 'site/signup_pm.html'

class SignUpParticipant(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('site/registration/login')
    template_name = 'site/signup_participant.html'

def pm_page(request):
    return render(request, 'site/pm.html')

def participant_page(request):
    return render(request, 'site/participant.html')


def about(request):
    return render(request, 'site/about.html')

# Create your views here.
