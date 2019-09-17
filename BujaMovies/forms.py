from django import forms
from .models import *
from django.contrib.auth.models import User

class FilmForm(forms.ModelForm):
    titre = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Titre ','class':'form-control'}), label='')
    acteur = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Acteur ','class':'form-control'}), label='')
    description = forms.CharField( widget = forms.Textarea( attrs = {'placeholder':'Description ','class':'form-control','rows':3,'cols':40} ), label='')
    language = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Language ','class':'form-control'}), label='')
    resolution = forms.IntegerField( widget=forms.NumberInput(attrs={'placeholder':'Resolution ','class':'form-control'}), label='')
    cover = forms.FileField( widget=forms.FileInput(attrs={'placeholder':'Affiche ','class':'form-control-file','class':'form-control'}), label='Cover')
    film = forms.FileField( widget=forms.FileInput(attrs={'placeholder':'Film ','class':'form-control-file','class':'form-control'}), label='Film')
    prix_telechargement = forms.IntegerField( widget=forms.NumberInput(attrs={'placeholder':'Prix ','class':'form-control'}), label='')
    class Meta:
        model = Films
        fields = ('titre','acteur','description','language','resolution','cover','film','prix_telechargement',)


class CommentaireForm(forms.Form):
    commentaire = forms.CharField( widget = forms.Textarea( attrs = {"rows":3,"cols":40} ))

class LikeForm(forms.ModelForm):
    class Meta:
        model = Avis
        exclude = ('user','slug_key',)

class InscriptionForm(forms.Form):
    pseudo = forms.CharField(label = "", max_length = 20, widget = forms.TextInput( attrs = {"placeholder":"Pseudo",'class':'form-control'} ) )
    email = forms.CharField(label = "", max_length = 50, widget = forms.EmailInput( attrs = {"placeholder":"Email",'class':'form-control'} ) )
    password1 = forms.CharField(label = "", max_length = 20, widget = forms.PasswordInput( attrs = {"placeholder":"Mot de pass",'class':'form-control'} ) )
    password2 = forms.CharField(label = "", max_length = 20 , widget = forms.PasswordInput( attrs = {"placeholder":"Confirmer mot de pass",'class':'form-control'} ) )

class ConnexionForm(forms.Form):
    pseudo = forms.CharField( label="", max_length = 20, widget = forms.TextInput( attrs = {"placeholder":"Pseudo",'class':'form-control'} ) )
    password1 = forms.CharField( label="", max_length = 20 , widget = forms.PasswordInput( attrs = {"placeholder":"Mot de pass",'class':'form-control'} ) )


    
