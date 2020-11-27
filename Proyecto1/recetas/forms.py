from django import forms
from django.db import models
from .models import Receta, Comment, Reports

class RecetasForm(forms.ModelForm):
    choices_state=(
        (1,'Activa'),
        (2,'Bloqueada'),
        )
    options= forms.ChoiceField(choices=choices_state,required=True, initial="Seleccione")
    class Meta:
        model = Receta
        fields = ('title', 'categoria', 'imagen','ingredients','text',)

class CommentForm(forms.ModelForm):
	author = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}), max_length = 200)
	class Meta:
		model = Comment
		fields = ('author','text',)


class ReportsForm(forms.ModelForm):
    informer = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}), max_length = 200)
    informed = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}), max_length = 200)
    choices_report=(
        (1,'Receta inválida'),
        (2,'Spam'),
        (3,'Otro'),
    )
    
    options= forms.ChoiceField(choices=choices_report,required=True, initial="Seleccione")
    
    class Meta:
        model= Reports
        fields=['informer','informed','options','text',]
