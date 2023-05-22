from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import  User

from user.models import KullaniciProfili

    
class KullaniciKayitFormu(UserCreationForm):
    username=forms.CharField (label =' Kullanıcı Adı :',max_length=50)
    first_name=forms.CharField(label='Ad :',max_length=50)
    last_name=forms.CharField(label='Soyad :',max_length=50)
    email =forms.EmailField(label='E-mail :',max_length=100)
    
    class Meta:
        model =User
        fields=('username','first_name','last_name','email','password1','password2')
        
        
class KullaniciGuncellemeFormu(UserChangeForm):
    class Meta:
        model = User
        fields = ( 'username','email','first_name','last_name')
        widgets = {
            'username'  : forms.TextInput(attrs={'class': 'input','placeholder':'username'}),
            'email'     : forms.EmailInput(attrs={'class': 'input','placeholder':'email'}),
            'first_name': forms.TextInput(attrs={'class': 'input','placeholder':'first_name'}),
            'last_name' : forms.TextInput(attrs={'class': 'input','placeholder':'last_name' }),
        }


CITY = [
    ('Istanbul', 'Istanbul'),
    ('Ankara', 'Ankara'),
    ('Izmir', 'Izmir'),
]
class ProfilGuncellemeFormu(forms.ModelForm):
    class Meta:
        model = KullaniciProfili
        fields = ('telefon', 'adres', 'sehir','ulke','image')
        widgets = {
            'telefon': forms.TextInput(attrs={'class': 'input','placeholder':'telefon'}),
            'adres' : forms.TextInput(attrs={'class': 'input','placeholder':'adres'}),
            'sehir' : forms.Select(attrs={'class': 'input','placeholder':'sehir'},choices=CITY),
            'ulke' : forms.TextInput(attrs={'class': 'input','placeholder':'ulke' }),
            'image' : forms.FileInput(attrs={'class': 'input', 'placeholder': 'image', }),
        }