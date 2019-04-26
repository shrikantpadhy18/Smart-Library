from django.db import models
from django.contrib.auth.models import(
    BaseUserManager,AbstractBaseUser
    )
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

status_choice1=(
    ('issued','ISSUED'),
    ('not_issued','NOT_ISSUED'),

    )
status_choice2=(
    ('returned','RETURNED'),
    ('not_returned','NOT_RETURNED'),
    )
class ITBooks(models.Model):
    author=models.TextField(null=False)
    bookname=models.CharField(max_length=130)
    year=models.CharField(max_length=2,default="")
    bookid=models.IntegerField(unique=True,
        validators=[MaxValueValidator(3000), MinValueValidator(1000)]
        )
    
    publisher=models.TextField(null=False)
class Books(models.Model):
    
    bookid=models.IntegerField(
        validators=[MaxValueValidator(9999), MinValueValidator(1000)]
        )
    branch=models.CharField(max_length=13,default="")
    rollno=models.CharField(max_length=8)
    issuingdate=models.DateField(("Date"), default=datetime.date.today)
    issuingstatus=models.CharField(default="",max_length=10,choices=status_choice1)
    returningstatus=models.CharField(default="",max_length=10,choices=status_choice2)
    DUE_DATE=models.DateField(models.DateField(("Date"),default=datetime.date.today))
    def details(self,request):
        rollno=request.user.username
    
class Image(models.Model):
    list=models.TextField(null=False)
class COMPSBooks(models.Model):
    
    author=models.TextField(null=False)
    bookname=models.CharField(max_length=130)
    year=models.CharField(max_length=2,default="")
    bookid=models.IntegerField(unique=True,
        validators=[MaxValueValidator(5000), MinValueValidator(3001)]
        )
   
    publisher=models.TextField(null=False)
     
class EXTCBooks(models.Model):
    
    author=models.TextField(null=False)
    bookname=models.CharField(max_length=130)
    year=models.CharField(max_length=2,default="")
    bookid=models.IntegerField(unique=True,
        validators=[MaxValueValidator(7000), MinValueValidator(5001)]
        )
   
    publisher=models.TextField(null=False)
    
class ELECTRONICSBooks(models.Model):
    
    author=models.TextField(null=False)
    bookname=models.CharField(max_length=130)
    year=models.CharField(max_length=2,default="")
    bookid=models.IntegerField(unique=True,
        validators=[MaxValueValidator(9000), MinValueValidator(7001)]
        )
   
    publisher=models.TextField(null=False)
class INSTRUBooks(models.Model):
    
    author=models.TextField(null=False)
    bookname=models.CharField(max_length=130)
    year=models.CharField(max_length=2,default="")
    bookid=models.IntegerField(unique=True,
        validators=[MaxValueValidator(9500), MinValueValidator(9001)]
        )

    publisher=models.TextField(null=False)
    
class searching(models.Model):
    year=models.CharField(max_length=12)

class BookId(models.Model):
    bookid=models.IntegerField(unique=True,
        validators=[MaxValueValidator(9999), MinValueValidator(1000)]
        )
class Branch(models.Model):
    branch=models.CharField(max_length=26)


class FE(models.Model):
    
    author=models.TextField(null=False)
    bookname=models.CharField(max_length=130)
    year=models.CharField(max_length=2,default="")
    bookid=models.IntegerField(unique=True,
        validators=[MaxValueValidator(9999), MinValueValidator(9501)]
        )

    publisher=models.TextField(null=False)

