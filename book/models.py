from ckeditor_uploader.fields import  RichTextUploadingField
from django.contrib.auth.models import User
from tkinter import CASCADE
from django.db import models
from django.utils.safestring import mark_safe #resimleri admnde göstermek için
from django.db.models import Avg, Count
from django.forms import ModelForm
from django.urls import reverse

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


# Create your models here.

class Category(MPTTModel): 
     STATUS = (
          ('True','Evet'),
          ('False','Hayır'),
     )

     title= models.CharField(blank=True,max_length=100)
     description= models.CharField(blank=True,max_length=100)
     keywords= models.CharField(blank=True,max_length=100)
     status= models.CharField(max_length=10,choices=STATUS) #açılır kutu şeklinde getirmek için
     slug= models.SlugField()
     #admin sayfasında yükleme yapmak için modül oluşturma
     image=models.ImageField(blank=True,upload_to='images/')
     parent= TreeForeignKey('self', related_name = 'children',blank=True,null=True, on_delete=models.CASCADE)
     create_at = models.DateField(auto_now_add=True)
     update_at = models.DateField(auto_now=True)
     lft=models.IntegerField(blank=True, null=True)
     rght=models.IntegerField(blank=True, null=True)
     #fonksiyon tanımlandıktan sonra title döndürecek.
     def __str__(self):
        return self.title
    
     class MPTTMeta:
        order_insertion_by = ['title']

     def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

     def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.title]                  # post.  use __unicode__ in place of
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])
   
   
   #kitap için database tanımlandı
class Books(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    VARIANTS = (
        ('None', 'None'),
        ('Karton Kapak', 'Karton Kapak'),
        ('Kuşe Kapak', 'Kuşe Kapak'),
        

    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #many to one relation with Category
    name =models.CharField(max_length=100,blank=False)
    title = models.CharField(max_length=150,blank=True)
    publisher=models.CharField(max_length=100,blank=False)
    #publication_date = models.DateField(blank=True)
    author = models.CharField(max_length=100,blank=False)
    num_of_pages = models.IntegerField(blank=True, null=True)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    quantity=models.IntegerField(default=0)
    minquantity=models.IntegerField(default=3)
    variant=models.CharField(max_length=50,choices=VARIANTS, default='None')
    ## detail = models.TextField()
    detail=RichTextUploadingField()
    slug = models.SlugField(null=False, unique=True)
    status=models.CharField(max_length=10,choices=STATUS)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    translated_by=models.CharField(blank=True,max_length=50)
    availability =models.BooleanField(default=True)
    image=models.ImageField(upload_to='images/',null=False)
    #cover_image =models.ImageField(upload_to='images/',null=False)
    
    def __str__(self):
        return str (self.name) 
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Resim'
    
class Resimler(models.Model) :
    books= models.ForeignKey(Books,on_delete=models.CASCADE)
    baslik = models.CharField(max_length=100,blank=True)  
    # resim = models.ImageField(blank=True,upload_to='images/')
    image=models.ImageField(blank=True,upload_to='images/',null=True)
    
    def __str__(self):
        return self.baslik
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Resim'
    
      
    
    

class Yorumlar(models.Model) :
    STATUS=(
        ('New','Yeni'),
        ('False','False'),
        ('True','True'),
        
    )
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    books= models.ForeignKey(Books,on_delete=models.CASCADE)
    konu= models.CharField(max_length=50, blank=True)
    yorum= models.CharField(max_length=300,blank=True)
    yorum_puani= models.IntegerField(default=1)
    durum =models.CharField(max_length=10,choices=STATUS, default='Yeni')
    ip = models.CharField(max_length=20, blank=True)
    olusturulma_zamani=models.DateTimeField(auto_now_add=True)
    guncellenme_zamani=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.konu
    
       