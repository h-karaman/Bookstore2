from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import  User



class AramaFormu(forms.Form):
    query = forms.CharField(max_length=100)
    #catid = forms.IntegerField()
    
class AuthorAramaFormu(forms.Form):
    q = forms.CharField(max_length=100)
