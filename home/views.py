from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from book.models import Category, Books, Resimler, Yorumlar
from home.models import IletisimFormu, IletisimMesaji, SayfaAyarlari

# Create your views here.

def index(request):
    sayfaayarlari = SayfaAyarlari.objects.get(pk=1)#sayfaayarlari kısmında pk kaç ise..
    sliderdata =Books.objects.all()[:3] #slider resimleri.üç tane alacak
    category = Category.objects.all()
    latestbooks =Books.objects.all().order_by('-id')[:8]  # 8 tane kitap sececek.
    booksforyou = Books.objects.all().order_by('?')[:8]   #rastgele 8 kitap sececek.
    categorybooks=Category.objects.all().order_by('?')[:8] 
    
    context ={'setting':sayfaayarlari,
              'page':'home',
              'sliderdata':sliderdata,
              'category':category,
              'latestbooks':latestbooks,
              'booksforyou':booksforyou,
              'categorybooks':categorybooks
              
              
             }
    
    return render (request,'index.html',context)


def hakkimizda(request):
    sayfaayarlari = SayfaAyarlari.objects.get(pk=1)#sayfaayarlari kısmında pk kaç ise..
    category=Category.objects.all()
    context ={'setting':sayfaayarlari,'page':'hakkimizda','category':category}
    return render (request,'hakkimizda.html',context)

def iletisim(request):
    
    if request.method == 'POST': # yöntemin post olup olmadığı kontrol ediliyor.
        form = IletisimFormu(request.POST)
        if form.is_valid():
            data = IletisimMesaji() #oluşturduğumuz modelle ilişkilendirme işlemi yapıyoruz.
            data.ad_soyad = form.cleaned_data['ad_soyad'] #formdan gelen verilerin alınması.
            data.email = form.cleaned_data['email']
            data.konu = form.cleaned_data['konu']
            data.mesaj = form.cleaned_data['mesaj']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  #burada formdan gelen veriler database e kaydediliyor.
            messages.success(request,"Mesajınız başarıyla iletildi.") #işlem başarılı ise mesaj veriliyor.
            return HttpResponseRedirect('/iletisim')

    
    sayfaayarlari = SayfaAyarlari.objects.get(pk=1) #sayfaayarlari kısmında pk kaç ise..
    form = IletisimFormu
    category =Category.objects.all()#iletsim sayfasında hata almamak için category de gönderilmeli!
    context={'setting':sayfaayarlari,'form':form ,'category':category }
    return render(request, 'iletisim.html', context)
 
def category_books(request,id,slug):
     category=Category.objects.all()
     #categorydata=Category.objects.get(pk=id)
     books = Books.objects.filter(category_id=id) 
     
     context={'books': books,'category':category}
     return render(request, 'category_books.html', context)
 
def book_detail(request,id,slug):
     category=Category.objects.all()
     book = Books.objects.filter(pk=id) 
     image = Resimler.objects.filter(books_id=id)
     yorumlar = Yorumlar.objects.filter(books_id=id,durum='True')#(% for rs in yorumlar %)
     context = {'book': book,'category':category,'slug':slug,
                'image': image,'yorumlar':yorumlar,
               
               }
     return render(request, 'book_detail.html', context)