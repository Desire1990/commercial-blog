from django import forms
from .models import *

class PayementForm(forms.Form):
	payementMethod = forms.IntegerField(label='Payement')
	montant = forms.IntegerField(label='Montant')
	identifiant = forms.IntegerField(label="Votre ID")