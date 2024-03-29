from django import forms
from .models import *

class PayementForm(forms.Form):
	payement_method = forms.IntegerField(label='Payement')
	montant = forms.IntegerField(label='Montant')
	identification = forms.IntegerField(label="Votre ID")

class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class MusicForm(forms.ModelForm):
	titre = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Titre ','class':'form-control'}), label='Titre')
	description = forms.CharField( widget = forms.Textarea( attrs = {'placeholder':'Description ','class':'form-control','rows':3,'cols':40} ), label='Description')
	audio = forms.FileField( widget=forms.FileInput(attrs={'placeholder':'Affiche ','class':'form-control-file','class':'form-control'}), label='Audio')
	cover = forms.FileField( widget=forms.FileInput(attrs={'placeholder':'Film ','class':'form-control-file','class':'form-control'}), label='Cover')
	price = forms.IntegerField( widget=forms.NumberInput(attrs={'placeholder':'Prix ','class':'form-control'}), label='Prix')
	class Meta:
		model = Music
		fields = ('audio', 'cover', 'owner', 'titre', 'description', "price")
		