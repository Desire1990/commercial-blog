from django import forms
from .models import *
# Create your models here.

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ("commentaire",)