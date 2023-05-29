
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from book.models import Books



# Create your models here.

class AlisverisSepeti(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Books, on_delete=models.SET_NULL, null=True)
    urun_adedi = models.IntegerField()
    
    def __str__(self):
        return str(self.book)#parantezi ve str yi unutma.yoksa 'str' hatası vercek.return self.book yazma.
    #self.book.title ya da .name yapınca hata veriyor.
    
    @property
    def price(self):
        return (self.book.price)#sepette fiyat yok.bunu book'tan alıp getirecek.

    @property
    def urun_tutari(self):
        return (self.book.price*self.urun_adedi  )

    


class AlisverisSepetiFormu(ModelForm):
    class Meta:
        model = AlisverisSepeti
        fields = ['urun_adedi']

class Siparis(models.Model):
    STATUS = (
        ('New', 'Yeni'),
        ('Accepted', 'Onaylandı'),
        ('Preparing', 'Hazırlanıyor'),
        ('OnShipping', 'Kargoya Verildi'),
        ('Completed', 'Tamamlandı'),
        ('Cancelled', 'İptal edildi'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    siparis_kodu = models.CharField(max_length=5, editable=False )
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    telefon = models.CharField(blank=True, max_length=20)
    adres = models.CharField(blank=True, max_length=150)
    sehir = models.CharField(blank=True, max_length=20)
    ulke = models.CharField(blank=True, max_length=20)
    alisveris_tutari = models.FloatField()
    durum=models.CharField(max_length=10,choices=STATUS,default='Yeni')
    ip = models.CharField(blank=True, max_length=20)
    bilginotu = models.CharField(blank=True, max_length=100)
    olusturulma_zamani=models.DateTimeField(auto_now_add=True)
    guncellenme_zamani=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name

class SiparisFormu(ModelForm):
    class Meta:
        model = Siparis
        fields = ['first_name','last_name','adres','telefon','sehir','ulke']

class SiparisUrunu(models.Model):
    STATUS = (
        ('New', 'Yeni'),
        ('Accepted', 'Onayla'),
        ('Cancelled', 'İptal Et'),
    )
    siparis = models.ForeignKey(Siparis, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    #variant = models.ForeignKey(Variants, on_delete=models.SET_NULL,blank=True, null=True) # relation with varinat
    urun_adedi = models.IntegerField()
    price = models.FloatField()
    urun_tutari = models.FloatField()
    durum = models.CharField(max_length=10, choices=STATUS, default='Yeni')
    olusturulma_zamani = models.DateTimeField(auto_now_add=True)
    guncellenme_zamani = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return str(self.book)
    
class FavoriSepeti(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Books, on_delete=models.SET_NULL, null=True)
    #urun_adedi = models.IntegerField()
    
    def __str__(self):
        return str(self.book)#parantezi ve str yi unutma.yoksa 'str' hatası vercek.return self.book yazma.
    #self.book.title ya da .name yapınca hata veriyor.
    
    
