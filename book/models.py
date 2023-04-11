
from django.db import models

# Create your models here.

class BookCategory(models.Model): 
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
     parent= models.ForeignKey('self', related_name = 'children',blank=True,null=True, on_delete=models.CASCADE)
     create_at = models.DateField(auto_now_add=True)
     update_at = models.DateField(auto_now=True)
     
     #fonksiyon tanımlandıktan sonra title döndürecek.
     def __str__(self):
        return self.title
   
   #kitap için databse tanımlandı
class Books(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    VARIANTS = (
        ('None', 'None'),
        ('Size', 'Size'),
        ('Color', 'Color'),
        ('Size-Color', 'Size-Color'),

    )
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE) #many to one relation with Category
    name =models.CharField(max_length=100,blank=False)
    title = models.CharField(max_length=150,blank=True)
    publisher=models.CharField(max_length=100,blank=False)
    #publication_date = models.DateField(blank=True)
    author = models.CharField(max_length=100,blank=False)
    num_of_pages = models.IntegerField(blank=True, null=True)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    #cover_image =models.ImageField(upload_to='images/',null=False)
    image=models.ImageField(upload_to='images/',null=False)
    price = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    quantity=models.IntegerField(default=0)
    minquantity=models.IntegerField(default=3)
    variant=models.CharField(max_length=10,choices=VARIANTS, default='None')
    detail=models.TextField()
    slug = models.SlugField(null=False, unique=True)
    status=models.CharField(max_length=10,choices=STATUS)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title   