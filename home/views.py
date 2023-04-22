from django.conf import Settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from book.models import Category, Books
from home.models import IletisimFormu, IletisimMesaji, SayfaAyarlari

# Create your views here.

def index(request):
    sayfaayarlari = SayfaAyarlari.objects.get(pk=1)#sayfaayarlari kısmında pk kaç ise..
    sliderdata =Books.objects.all()[:3] #slider resimleri.üç tane alacak
    category = Category.objects.all()
    context ={'setting':sayfaayarlari,
              'page':'home',
              'sliderdata':sliderdata,
             'category':category
             }
    
    return render (request,'index.html',context)


def hakkimizda(request):
    sayfaayarlari = SayfaAyarlari.objects.get(pk=1)#sayfaayarlari kısmında pk kaç ise..
    context ={'setting':sayfaayarlari,'page':'hakkimizda'}
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
    context={'setting':sayfaayarlari,'form':form  }
    return render(request, 'iletisim.html', context)
