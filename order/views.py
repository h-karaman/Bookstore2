from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.utils.crypto import get_random_string


from order.models import AlisverisSepeti, AlisverisSepetiFormu, SiparisFormu, Siparis,SiparisUrunu
from book.models import Category, Books
from user.models import KullaniciProfili


def index(request):
    return HttpResponse ("Siparis Sayfası")

@login_required(login_url='/login') # Kullanıcı login mi?kontrol ediyor.
def sepeteekle(request,id):
    sonurl = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Kullanıcının session bilgilerlini alıyoruz.
    #book= Books.objects.get(pk=id)

    
    
    urun_sepette_mi = AlisverisSepeti.objects.filter(book_id=id, user_id=current_user.id) # Check product in shopcart
    if urun_sepette_mi:
            sepette = 1 # Ürün alışveriş sepetinde var demektir.
    else:
            sepette = 0 # Ürün alışveriş sepetinde yok demektir.

    if request.method == 'POST':  # request metodu post ise...
        form = AlisverisSepetiFormu(request.POST)
        if form.is_valid():
            if sepette==1: # alışveriş sepeti guncelleme
                
                data = AlisverisSepeti.objects.get(book_id=id, user_id=current_user.id)
                
                    
                data.urun_adedi += form.cleaned_data['urun_adedi']
                data.save()  # save data
            else : # Alışveriş sepetinde yok.sepete eklenecek.
                data = AlisverisSepeti()
                data.user_id = current_user.id
                data.book_id =id
                
                data.urun_adedi = form.cleaned_data['urun_adedi']
                data.save()
        messages.success(request, "Ürün sepete eklendi. ")
        
        return HttpResponseRedirect(sonurl)

    else: # formdan veri alınmayıp,ana sayfaddan direkt sepete ekleme yapılacaksa vb.
        if sepette == 1:  # sepet güncellenecek(ürün sepette varsa)
            data = AlisverisSepeti.objects.get(book_id=id, user_id=current_user.id)
            data.urun_adedi += 1
            data.save()  #
        else:  #  Ürün sepete eklenecek(ürün sepette yoksa)
            data = AlisverisSepeti()  # model ile bağlantı kurulacak.
            data.user_id = current_user.id
            data.book_id = id
            data.urun_adedi = 1# bir adet ürün sepete eklenecek.ana sayfadan 1 tane ekleme şansımız var.
            
            data.save()  #veriler kaydediliyor.
        messages.success(request, "Ürün alışveriş sepetine eklendi.")
        return HttpResponseRedirect(sonurl) #en son ürün  ekleme yaptığımız url e dönüyor.


def alisverissepeti(request):
    category = Category.objects.all()
    current_user = request.user  # kullanıcının session bilgileri alınıyor.
    alisverissepeti = AlisverisSepeti.objects.filter(user_id=current_user.id)
    alisveris_tutari=0
    for rs in alisverissepeti:
        alisveris_tutari += rs.book.price * rs.urun_adedi
    #return HttpResponse(str(total))
    
    context={'alisverissepeti': alisverissepeti,
             'category':category,
             'alisveris_tutari': alisveris_tutari,
             }
    return render(request,'alisverissepeti_urunleri.html',context)


@login_required(login_url='/login') # Kullanıcı login mi?kontrol ediyor.
def sepeti_guncelle_artir(request,id):
    sonurl = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Kullanıcının session bilgilerlini alıyoruz.
    #book= Books.objects.get(id=id)
    data = AlisverisSepeti.objects.get(id=id, user_id=current_user.id)
    data.urun_adedi += 1
    data.save()  #
    return HttpResponseRedirect(sonurl)
       
@login_required(login_url='/login') # Kullanıcı login mi?kontrol ediyor.
def sepeti_guncelle_azalt(request,id):
    sonurl = request.META.get('HTTP_REFERER')  # en son bulunduğumuz url'i alıyor.
    current_user = request.user  # Kullanıcının session bilgilerlini alıyoruz.
    #book= Books.objects.get(pk=id)
    #id=id olmasına dikkat et.
    #yoksa sepette en alttaki ürün ile ilgili işlem yapıyor!!!!
    #ürün id'si gelmeli.
    data = AlisverisSepeti.objects.get(id=id, user_id=current_user.id)
    if data.urun_adedi== 1:
        data=AlisverisSepeti.objects.filter(id=id).delete()
        #sorgu önemli.bu şekilde olmazsa sepet guncellenemeyecek!!!!
        #save yapma ...yoksa 0 olarak kaydeder.
    else:   
        data.urun_adedi -= 1
        data.save() #database e kaydedecek.
        messages.success(request, "Ürün adedi azaltıldı.")
    return HttpResponseRedirect(sonurl)        
        
    
    
    
    
# Kullanıcının login olup olmadığı kontrol ediliyor.Giriş yapmış olmalı..
#giriş yapmamışsa login sayfasına yönlendirilecek.
@login_required(login_url='/login') 
#kullanıcı giriş yapmışsa sepetten çıkarmaya gidecek.
def sepettencikar(request,id):
    AlisverisSepeti.objects.filter(id=id).delete()
    messages.success(request, "Ürün sepetten çıkartıldı.")
    return HttpResponseRedirect("/alisverissepeti")


def siparisurunu(request):
    category = Category.objects.all()
    current_user = request.user
    alisverissepeti = AlisverisSepeti.objects.filter(user_id=current_user.id)
    
    alisveris_tutari = 0
    for rs in alisverissepeti:
        
        alisveris_tutari += rs.book.price * rs.urun_adedi
        
 
    if request.method == 'POST': 
        form = SiparisFormu(request.POST)
        #return HttpResponse(request.POST.items())
        if form.is_valid():
            data = Siparis()
            data.first_name = form.cleaned_data['first_name'] #get product quantity from form
            data.last_name = form.cleaned_data['last_name']
            data.adres = form.cleaned_data['adres']
            data.sehir = form.cleaned_data['sehir']
            data.telefon = form.cleaned_data['telefon']
            data.user_id = current_user.id
            data.alisveris_tutari = alisveris_tutari
            data.ip = request.META.get('REMOTE_ADDR')
            siparis_kodu= get_random_string(10).upper() # random cod
            data.code =  siparis_kodu
            data.save() #


            for rs in alisverissepeti:
                detail = SiparisUrunu()
                detail.siparis_id=data.id # Order Id
                detail.book_id= rs.book_id
                detail.user_id= current_user.id
                detail.urun_adedi= rs.urun_adedi
                detail.price= rs.book.price
                detail.urun_tutari = rs.book.price * rs.urun_adedi
                detail.save()
                # ***Reduce quantity of sold product from Amount of Product
                
                book = Books.objects.get(id=rs.book_id)
                book.quantity -= rs.urun_adedi
                book.save()
                
                #************ <> *****************

            AlisverisSepeti.objects.filter(user_id=current_user.id).delete() # Clear & Delete shopcart
            request.session['cart_items']=0
            messages.success(request, "Siparişiniz tamamlandı. ")
            return render(request, 'siparis_tamamlandi.html',{'siparis_kodu':siparis_kodu,'category': category})
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect("/order/siparisurunu")

    form= SiparisFormu()
    kullanici_profili = KullaniciProfili.objects.get(user_id=current_user.id)
    context = {'alisverissepeti': alisverissepeti,
               'category': category,
               'alisveris_tutari': alisveris_tutari,
               'form': form,
               'kullanici_profili': kullanici_profili,
               }
    return render(request, 'siparis_formu2.html', context)

@login_required(login_url='/login') # Kullanıcı login mi?kontrol ediyor.
def sepetiguncelle(request,id):
    sonurl = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Kullanıcının session bilgilerlini alıyoruz.
    book= Books.objects.get(pk=id)

    if request.method == 'POST':  # request metodu post ise...
        form = AlisverisSepetiFormu(request.POST)
        if form.is_valid():
            
                 
            data = AlisverisSepeti.objects.filter(book_id=id, user_id=current_user.id)
            for rs in data:
                  
             rs.urun_adedi = form.cleaned_data['urun_adedi']
             rs.save()  # save data
           
        messages.success(request, "Ürün sepete eklendi. ")
        
        return HttpResponseRedirect(sonurl)

    