from .views import *
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home, name='home'),
    #path('home/', views.home, name='home'),
    #path('signup/', views.SignUpGeneral.as_view(), name='signup'),
    #path('signup_pm/', views.SignUpPM.as_view(), name='signup_pm'),
    #path('signup_participant/', views.SignUpParticipant.as_view(), name='signup_participant'),
    path('participant/', participant_page, name='participant_page'),
    path('pm/', pm_page, name='pm_page'),
    path('upload/', upload, name='upload'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('data/', data, name='data'),
    path('reg/', reg, name='reg'),
    #path('description/<slug:description_slug>/', show_post, name='desription'),
    #path('type/<int:type_id>/', show_category, name='type'),
]

