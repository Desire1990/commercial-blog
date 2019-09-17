from django import forms
from .models import *

class PayementForm(forms.Form):
	payement_method = forms.IntegerField(label='Payement')
	montant = forms.IntegerField(label='Montant')
	identification = forms.IntegerField(label="Votre ID")


class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)