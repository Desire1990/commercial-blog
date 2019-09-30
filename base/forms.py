from django import forms
from .models import *
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    name = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Full name ','class':'form-control'}), label='')
    tel = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Phone number ','class':'form-control'}), label='')
    email = forms.EmailField( widget = forms.TextInput( attrs = {'placeholder':'Email adress ','class':'form-control','rows':3,'cols':40} ), label='')
    message = forms.CharField( widget=forms.Textarea(attrs={'placeholder':'Tapez ici votre message . . . ','class':'form-control'}), label='')
    
    class Meta:
        model = Contact
        fields = ('name','tel','email','message')

class ConnexionForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'User name ','class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password ', 'type':'password','class':'form-control'}))

class InscriptionForm(forms.Form):
    username = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'username ','class':'form-control'}), label='username')
    password = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'password ','class':'form-control'}), label='password')
    password2 = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'confirm password ','class':'form-control'}), label='confirm password')
    email = forms.EmailField( widget = forms.TextInput( attrs = {'placeholder':'email adress ','class':'form-control'} ), label='your email adress')
    avatar = forms.ImageField( widget=forms.FileInput(attrs={'class':'form-control'}), label='your profile picture')
 