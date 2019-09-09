from django import forms
from .models import *
from django.contrib.auth.models import User

class FilmForm(forms.ModelForm):
    class Meta:
        model = Films
        fields = ('titre','acteur','description','language','resolution','cover','film','prix_telechargement',)

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaires
        fields = ('commentaire',)

class AvisForm(forms.ModelForm):
    class Meta:
        model = Avis
        exclude = ('user','likes','dislikes','slug_key',)

class InscriptionForm(forms.Form):
    pseudo = forms.CharField(label = "Pseudo", max_length = 20 )
    email = forms.CharField(label = "Email", max_length = 50 )
    password1 = forms.CharField(label = "Mot de pass", max_length = 20, widget = forms.PasswordInput )
    password2 = forms.CharField(label = "Comfirmer mot de pass", max_length = 20 , widget = forms.PasswordInput )


class ConnexionForm(forms.Form):
    pseudo = forms.CharField(label = "Pseudo", max_length = 20 )
    password1 = forms.CharField(label = "Mot de pass", max_length = 20 , widget = forms.PasswordInput )


    
