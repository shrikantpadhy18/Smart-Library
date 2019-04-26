
from django.contrib import admin
from django.urls import path,include
from forum.views import register,logout_request,login_request,homepage,aflogin,Compsbooks,search,searchy
app_name="main"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register),
   path('logout/',logout_request,name="logout"),
   path('login/',login_request,name="login"),

    path('', homepage, name="homepage"),
    path('',include('django.contrib.auth.urls')),
    path('aflogin/',aflogin,name="aflogin"),
    path('Compsbooks/',Compsbooks,name="Compsbooks"),
    
    path('search/',search),
    path('searchy/',searchy),
    path('forum/',include('forum.urls')),
]
