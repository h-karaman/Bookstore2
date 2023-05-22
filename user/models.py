from django.db import models

from ckeditor_uploader.fields import  RichTextUploadingField
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


# Create your models here.

class KullaniciProfili(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    ulke=models.CharField(blank=True,max_length=30)
    sehir=models.CharField(blank=True,max_length=30)
    adres=models.CharField(blank=True,max_length=100)
    telefon=models.CharField(blank=True,max_length=30)
    #kullanıcıların resmi /users/ klasörüne eklenebilir.(asagıda tanımlı image path.)
    image= models.ImageField(blank=True,upload_to='images/users/')
    
    def __str__(self):
        return self.user.username
    
    def kullanici_adi(self):
        return self.user.first_name +' '+ self.user.last_name
    
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Resim'
    
class KullaniciProfiliFormu(ModelForm):
    class Meta:
        model = KullaniciProfili
        fields = ['ulke', 'sehir', 'adres','telefon','image']
