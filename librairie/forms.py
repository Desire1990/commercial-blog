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

class BookForm(forms.ModelForm):
	titre = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Titre ','class':'form-control'}))
	description = forms.CharField( widget = forms.Textarea( attrs = {'placeholder':'Description ','class':'form-control','rows':3,'cols':40} ))
	categorie = forms.ModelChoiceField( 
		widget = forms.Select( 
			attrs = {'placeholder':'categorie ','class':'form-control'}
			),
		queryset=Categorie.objects.all()
		)
	maison = forms.CharField( widget = forms.TextInput( attrs = {'placeholder':'maison ','class':'form-control'} ))
	prix = forms.IntegerField( widget=forms.NumberInput(attrs={'placeholder':'prix ','class':'form-control'}))
	version = forms.IntegerField( widget=forms.NumberInput(attrs={'placeholder':'version ','class':'form-control'}))
	cover = forms.ImageField( widget=forms.ClearableFileInput(attrs={'class':'form-control-file'}))
	livre = forms.FileField( widget=forms.ClearableFileInput(attrs={'class':'form-control-file'}))
	class Meta:
		model = Livre
		fields = ("titre", "description", "maison", "categorie", 
        	"annee", "prix", "livre", "cover", "version")