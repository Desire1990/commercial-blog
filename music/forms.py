from django import forms
from .models import *


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class PayementForm(forms.Form):
	payementMethod = forms.IntegerField(label='Payement')
	montant = forms.IntegerField(label='Montant')
	identifiant = forms.IntegerField(label="Votre ID")