from django.forms import ModelForm
from django import forms
from models import Collection, Card
from django.contrib.auth.forms import UserCreationForm

class CollectionForm(ModelForm):
	class Meta:
		model = Collection

class CardForm(ModelForm):
	class Meta:
		model = Card

class EmailUserCreationForm(UserCreationForm):
	email = forms.EmailField()
