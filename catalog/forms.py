# from catalog.models import Book,Author,BookInstance,Genre
from dataclasses import field
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . models import *

class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ['author','title', 'summary', 'isbn' , 'genre']

class RegFrom(forms.ModelForm):
    
    class Meta:
        model = Author
        field = '__all__'
        exclude = ['user']

class SignupForm(UserCreationForm):
    username = forms.CharField(label='username', required=True)
    first_name = forms.CharField(label='first name', required=True)
    last_name = forms.CharField(label='last name', required=True)
    email = forms.EmailField(label='email', required=True)
    password1 = forms.CharField(label='Enter password',required=True,widget=forms.PasswordInput(attrs={'type':'password'}))
    password2 = forms.CharField(label='confirm password',required=True,widget=forms.PasswordInput(attrs={'type':'password'}))
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email','password1','password2']


