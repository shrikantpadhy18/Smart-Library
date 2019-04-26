from django.shortcuts import render,redirect
from .forms import post, productform
from django.http  import HttpResponse
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from . models import Books,Branch,BookId
from django.db.models import Q
from . models import ITBooks,COMPSBooks, EXTCBooks,ELECTRONICSBooks,INSTRUBooks
from . models import Books,FE
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from . forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib import messages
from . models import Image
def homepage(request):
    image=Image.objects.all()
    return render(request,"base1.html",{'image':image})
def bookissue(request):
    posts=productform()
    if request.method=="POST":
        posts=productform(request.POST)
        
        if posts.is_valid() :
            p=posts.cleaned_data['branch']
            r=posts.cleaned_data['bookid']
            mat1=Branch.objects.filter(Q(branch__iexact=p))
            mat2=BookId.objects.filter(Q(bookid__iexact=r))

            if mat1 and mat2:
                posts.cleaned_data['rollno']=request.user.username
                Books.objects.create(**posts.cleaned_data)
                return HttpResponse("<h1>REQUEST SUBMITTED SUCCESSFULLY")
            else:
                return HttpResponse("<h1>INVALID BOOKID OR BRANCH")

        else:
            return HttpResponse("<h1>YOU HAVE ENTERED INVALID DATA")
    mycontext={
        'posts':posts
    }
    return render(request,"file1.html",mycontext)
def search(request):
    if request.method=='POST':
       
        srch = request.POST.get('srh', False)

        if srch:
            match6=FE.objects.filter(Q(bookname__istartswith=srch) | Q(bookid__startswith=srch))
            match1=ITBooks.objects.filter(Q(bookname__istartswith=srch) | Q(bookid__startswith=srch) | Q(year__icontains=srch))

            match2=COMPSBooks.objects.filter(Q(bookname__istartswith=srch) | Q(bookid__startswith=srch) | Q(year__icontains=srch))

            match3=ELECTRONICSBooks.objects.filter(Q(bookname__istartswith=srch) | Q(bookid__startswith=srch) | Q(year__icontains=srch))

            match4=EXTCBooks.objects.filter(Q(bookname__istartswith=srch) | Q(bookid__startswith=srch) | Q(year__icontains=srch))

            match5=INSTRUBooks.objects.filter(Q(bookname__istartswith=srch) | Q(bookid__startswith=srch) | Q(year__icontains=srch))

            if match6:
                return render(request,'Compbooks.html',{'sr':match6})

            elif match1:
                return render(request,'Compbooks.html',{'sr':match1})

            elif match2:
                return render(request,'Compbooks.html',{'sr':match2})

            elif match3:
                return render(request,'Compbooks.html',{'sr':match3})
            elif match4:
                return render(request,'Compbooks.html',{'sr':match4})

            elif match5:
                return render(request,'Compbooks.html',{'sr':match5})

            else:
                messages.error(request,"BOOK NOT FOUND")

        else:
            return HttpResponse('/search/')

    return render(request,'Compbooks.html')

def register(request):
    form = NewUserForm
    if request.method=="POST":
        form=NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            FIRSTNAME=form.cleaned_data.get('FIRSTNAME')
            LASTNAME = form.cleaned_data.get('LASTNAME')
            EMAIL = form.cleaned_data.get('EMAIL')
            user.save()
            #ROLLNO = form.cleaned_data.get('ROLLNO')
           # student.objects.create(**form.cleaned_data)
            #messages.info(request,"new account created:",request.user.username)
            login(request,user)
            #messages.info(request,"you are now logged in as %s",request.user.username)
            return redirect("http://127.0.0.1:8000/aflogin/")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
    return  render(request,
                 "registration_form.html",
                   context={'form':form },
    )
def logout_request(request):
    logout(request)
    return redirect("http://127.0.0.1:8000")
def login_request(request):
    form=AuthenticationForm
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("http://127.0.0.1:8000/aflogin/")
            else:
                pass
    else:
        pass


    return render(request,"login.html",{'form':form})


def aflogin(request):
    
    return render(request,"aflogin.html",{'so':request})

def Compsbooks(request):
    pro=COMPSBooks.objects.all()
    return render(request,"Compbooks.html",{'pro':pro})

def fe(request):
    pro=FE.objects.all()
    return render(request,"Compbooks.html",{'pro':pro})

def Itbooks(request):
    pro=ITBooks.objects.all()
    return render(request,"Compbooks.html",{'pro':pro})

def Elecbooks(request):
    pro=ELECTRONICSBooks.objects.all()
    return render(request,"Compbooks.html",{'pro':pro})


def Extbooks(request):
    pro=EXTCBooks.objects.all()
    return render(request,"Compbooks.html",{'pro':pro})

def Instrubooks(request):
    pro=INSTRUBooks.objects.all()
    return render(request,"Compbooks.html",{'pro':pro})



def About(request):
    return render(request,"check.html")

def IssuingStatus(request):
    pro=Books.objects.all()
    return render(request,"soap.html",{'pro':pro})



def searchy(request):
    if request.method=='POST':
       
        srch = request.POST.get('srh', False)

        if srch:
            match1=Books.objects.filter(Q(rollno__icontains=srch) | Q(bookid__contains=srch))

            if match1:
                return render(request,'soap.html',{'sr':match1})

            else:
                 messages.error(request,"RESULT NOT FOUND")

        else:
            return HttpResponse('/searchy/')

    return render(request,'soap.html')

