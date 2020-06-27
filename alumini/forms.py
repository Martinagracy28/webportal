from django import forms
from django.forms import ModelForm
from .models import *

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = '__all__'

class AluminiForm(forms.ModelForm):
    class Meta:
        model = Alumini
        fields = '__all__'        
        
