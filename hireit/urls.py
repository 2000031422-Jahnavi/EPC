
from django.urls import path
from hireit.views import *

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login,name='login'),
    path('newuserregister/', views.newuserregister,),
    path('home/', views.home,),
    path('about/', views.about,),
    path('services/', views.services,),
    path('job/', views.job,),
    path('contact/', views.contact,),
    path('applicationform/',views.applicationform,),
    path('signout/',views.signout,),
    path('statistics/',views.statistics,),

   


]