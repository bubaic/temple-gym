from django import forms

from .models import User


class SignupForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['user', 'first_name', 'last_name']
