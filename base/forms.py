from django import forms
from .models import *
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    name = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'full name ','class':'form-control'}), label='')
    tel = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'phone number ','class':'form-control'}), label='')
    email = forms.EmailField( widget = forms.TextInput( attrs = {'placeholder':'email adress ','class':'form-control','rows':3,'cols':40} ), label='')
    message = forms.CharField( widget=forms.Textarea(attrs={'placeholder':'Language ','class':'form-control'}), label='')
    
    class Meta:
        model = Contact
        fields = ('name','tel','email','message')

class ConnexionForm(forms.Form):
    pseudo = forms.CharField( label="", max_length = 20, widget = forms.TextInput( attrs = {"placeholder":"Pseudo",'class':'form-control'} ) )
    password1 = forms.CharField( label="", max_length = 20 , widget = forms.PasswordInput( attrs = {"placeholder":"Mot de pass",'class':'form-control'} ) )


    
