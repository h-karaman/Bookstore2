from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from book.models import Books
from home.models import IletisimFormu, IletisimMesaji, SayfaAyarlari

# Create your views here.
def index(request):
    sayfaayarlari = SayfaAyarlari.objects.get(pk=4)
    sliderdata =Books.objects.all()[:3]
    context ={'setting':sayfaayarlari,'page':'home','sliderdata':sliderdata}
    return render (request,'index.html',context)


def hakkimizda(request):
    sayfaayarlari = SayfaAyarlari.objects.get(pk=4)
    context ={'setting':sayfaayarlari,'page':'hakkimizda'}
    return render (request,'hakkimizda.html',context)

def iletisim(request):
    
    if request.method == 'POST': # check post
        form = IletisimFormu(request.POST)
        if form.is_valid():
            data = IletisimMesaji() #create relation with model
            data.ad_soyad = form.cleaned_data['ad_soyad'] # get form input data
            data.email = form.cleaned_data['email']
            data.konu = form.cleaned_data['konu']
            data.mesaj = form.cleaned_data['mesaj']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  #save data to table
            messages.success(request,"Mesajınız başarıyla iletildi.")
            return HttpResponseRedirect('/iletisim')

    
    sayfaayarlari = SayfaAyarlari.objects.get(pk=4)
    form = IletisimFormu
    context={'setting':sayfaayarlari,'form':form  }
    return render(request, 'iletisim.html', context)
