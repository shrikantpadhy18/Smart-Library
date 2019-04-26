from . models import Books,searching
from django import forms
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxValueValidator, MinValueValidator
class post(forms.ModelForm):
    class Meta:
        model=Books
        fields=[
            'branch',
            'bookid',
            'rollno',
        ]
class NewUserForm(UserCreationForm):
    EMAIL=forms.EmailField(required=True)
    FIRSTNAME=forms.CharField(required=True)
    LASTNAME = forms.CharField(required=True)

    #ROLLNO=forms.CharField(required=True)
    class Meta:
        model=User
        fields=['FIRSTNAME','LASTNAME','username','EMAIL','password1','password2']
    def save(self,commit=True):
        user=super(NewUserForm,self).save(commit=False)
        user.FIRSTNAME=self.cleaned_data['FIRSTNAME']
        user.LASTNAME=self.cleaned_data['LASTNAME']
        #user.ROLLNO=self.cleaned_data['ROLLNO']
        user.EMAIL = self.cleaned_data['EMAIL']
        user.username=self.cleaned_data['username']
        if commit:
            user.save()
        return user

class productform(forms.Form):
    
    bookid = forms.IntegerField(required=True,
        validators=[MaxValueValidator(9999), MinValueValidator(1000)],
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": 'bookid',
                                       'cols': 5,
                                       'rows': 2
                                   }
                               )

                               )
    branch = forms.CharField(required=True,
                             widget=forms.TextInput(
                                 attrs={
                                     "placeholder": 'branch',
                                     'cols': 5,
                                     'rows': 2
                                 }
                             )
                             )