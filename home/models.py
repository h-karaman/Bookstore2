from django.db import models
from ckeditor_uploader.fields import  RichTextUploadingField
from django.forms import ModelForm, TextInput, Textarea
# Create your models here.

# Sayfa ayarları için örnek model olşturulur.

class SayfaAyarlari(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    firma = models.CharField(max_length=200)
    adres = models.CharField(blank=True,max_length=100)
    telefon = models.CharField(blank=True,max_length=15)
    fax = models.CharField(blank=True,max_length=15)
    email = models.CharField(blank=True,max_length=50)
    smtpport = models.CharField(blank=True,max_length=5)
    smtpserver = models.CharField(blank=True,max_length=50)
    smtppassword = models.CharField(blank=True,max_length=10)
    smtpemail = models.CharField(blank=True,max_length=50)
    icon = models.ImageField(blank=True,upload_to='images/')
    instagram = models.CharField(blank=True,max_length=50)
    twitter = models.CharField(blank=True,max_length=50)
    facebook = models.CharField(blank=True,max_length=50)
    youtube = models.CharField(blank=True, max_length=50)
    hakkimizda = RichTextUploadingField()
    iletisim = RichTextUploadingField()
    referanslar = RichTextUploadingField()
    status=models.CharField(max_length=10,choices=STATUS)
    olusturulma_zamani=models.DateTimeField(auto_now_add=True)
    guncellenme_zamani=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




class IletisimMesaji(models.Model):
    STATUS = (
        ('New', 'Yeni'),
        ('Read', 'Okundu'),
        ('Closed', 'Kapandı'),
    )
    ad_soyad= models.CharField(blank=True,max_length=30)
    email= models.CharField(blank=True,max_length=50)
    konu= models.CharField(blank=True,max_length=50)
    mesaj= models.TextField(blank=True,max_length=300)
    durum=models.CharField(max_length=10,choices=STATUS,default='Yeni')
    ip = models.CharField(blank=True, max_length=20)
    not_ekle= models.CharField(blank=True, max_length=100)
    olusturulma_tarihi=models.DateTimeField(auto_now_add=True)
    guncellenme_tarihi=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ad_soyad

class IletisimFormu(ModelForm):
    class Meta:
        model = IletisimMesaji
        fields = ['ad_soyad', 'email', 'konu','mesaj']
        widgets = {
            'ad_soyad'   : TextInput(attrs={'class': 'input','placeholder':'Ad-Soyad','required':True }),
            'email'   : TextInput(attrs={'class': 'input','placeholder':'Email Adresi','required':True}),
            'konu' : TextInput(attrs={'class': 'input','placeholder':'Konu','required':True}),
            'mesaj' : Textarea(attrs={'class': 'input','placeholder':'Mesajınız','rows':'7'}),
        }