from . import views
from django.urls import path, include
#from .views import  participant_page, hr_page, pm_page

urlpatterns = [
    path('', views.home, name='home'),
    #path('home/', views.home, name='home'),
    path('signup/', views.SignUpGeneral.as_view(), name='signup'),
    #path('signup_hr/', views.SignUpHR.as_view(), name='signup_hr'),
    path('signup_pm/', views.SignUpPM.as_view(), name='signup_pm'),
    path('signup_participant/', views.SignUpParticipant.as_view(), name='signup_participant'),
    path('participant/', views.participant_page, name='participant_page'),
    path('pm/', views.pm_page, name='pm_page'),
    path('about/', views.about, name='about'),
    path('login/', views.about, name='login'),
    path('data/', views.about, name='data'),
    path('reg/', views.about, name='reg'),

    #path('hr/', hr_page, name='hr_page'),
]

