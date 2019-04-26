from django.urls import path
from django.contrib import admin
from .views import register,logout_request,login_request,bookissue,Itbooks,Elecbooks,Extbooks,Instrubooks,About,IssuingStatus,search,searchy,fe
urlpatterns = [
   path('register/',register),
   path('logout/',logout_request,name="logout"),
   path('login/',login_request,name="login"),
   path('bookissue/',bookissue,name="bookissue"),
   
   path('Itbooks/',Itbooks,name="Itbooks"),
   path('Elecbooks/',Elecbooks,name="Elecbooks"),
   path('Extbooks/',Extbooks,name="Extbooks"),
   path('About/',About,name="About"),
   path('Instrubooks/',Instrubooks,name="Instrubooks"),
   path('IssuingStatus/',IssuingStatus,name="IssuingStatus"),
   path('fe/',fe,name="fe"),
   path('search/',search,name="search"),
   path('searchy/',searchy,name="searchy"),
   
]
