from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField

class CustomUserForm(UserCreationForm):
	email = forms.EmailField(max_length=200, help_text='Required')
	first_name = forms.CharField(label="Nombre", help_text='Required')
	last_name = forms.CharField(label="Apellido", help_text='Required')
	captcha = ReCaptchaField()
	class Meta:
		model = User
		fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')
