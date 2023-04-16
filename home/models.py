from django.db import models

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
    hakkimizda = models.TextField(blank=True,max_length=300)
    iletisim = models.TextField(blank=True,max_length=50)
    referanslar = models.TextField(blank=True,max_length=50)
    status=models.CharField(max_length=10,choices=STATUS)
    olusturulma_zamani=models.DateTimeField(auto_now_add=True)
    guncellenme_zamani=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




