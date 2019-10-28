from django import forms
from .models import Post, Comment

class CommentForm(forms.Form):
	class meta:
		model = Comment
		fields = ('name','email','comment')


# pour eviter meme la validation de quoi que ce soit, declare une f(x) clean suivi du champ:
	def clean_message(self):
		message = self.cleaned_data['message']
		if "quelq choses d'injures in message":
			forms.validationError('On ne veut pas entendre ce type de message ici')

		return message


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','slug', 'author','status','stock', 'image_url','categorie','content', 'price')
		