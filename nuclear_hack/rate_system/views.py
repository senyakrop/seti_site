from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, logout
from .forms import *
from .models import *
from .utils import *

#menu = ["Login", "Registration", "Data", "About"]

menu = [{'title': "Data", 'url_name': 'data'},
        {'title': "About", 'url_name': 'about'}]



def home(request):
    if (request.user.is_authenticated):
        return render(request, 'site/home.html', {'title':'home', 'menu':menu})
    else:
        return redirect('/login/')
    #return render(request, 'site/home.html', {'title': 'home', 'menu': menu})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
    #return redirect('/', permanent=True)


class SignUpGeneral(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'site/reg.html'

def pm_page(request):
    return render(request, 'site/pm.html')

def participant_page(request):
    return render(request, 'site/participant.html')


def about(request):
    return render(request, 'site/about.html', {'title': 'about', 'menu': menu})


def reg(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # сохранение номера
            Utype.objects.create(user=user, type=form.cleaned_data.get('type'))
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'site/reg.html', {'title': 'registration', 'form': form, 'menu': menu})


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'registration/login.html'
    #extra_context = {'title': 'login'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'login'
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
# Create your views here.
