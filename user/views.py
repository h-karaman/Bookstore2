from django.http import HttpResponse,HttpResponseRedirect
from book.models import Books, Category, Yorumlar
from django.shortcuts import render
from home.models import SayfaAyarlari
from order.models import AlisverisSepeti, FavoriSepeti, Siparis, SiparisUrunu
from user.forms import KullaniciGuncellemeFormu, KullaniciKayitFormu, ProfilGuncellemeFormu
from user.models import KullaniciProfili
from django.contrib.auth.models import User 
import json
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth import update_session_auth_hash
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm


# Create your views here.
def index(request):
    category=Category.objects.all()
    current_user=request.user
    sayfaayarlari = SayfaAyarlari.objects.get(pk=1)#sayfaayarlari kısmında pk kaç ise..
    alisverissepeti = AlisverisSepeti.objects.filter(user_id=current_user.id)#ana sayfada alışveriş sepeti
    favorisepeti = FavoriSepeti.objects.filter(user_id=current_user.id)#ana sayfada favori sepeti
    #şu an login olan kullanıcının id'sini almak için..
    kullaniciprofili=KullaniciProfili.objects.get(user_id=current_user.id)
    context ={'category':category,'kullaniciprofili':kullaniciprofili,
           'sayfaayarlari':sayfaayarlari,'alisverissepeti':alisverissepeti,'favorisepeti': favorisepeti ,
           }
    return render (request,'kullanici_profili.html',context)



def kayitol_view(request):
        if request.method=='POST':
            form = KullaniciKayitFormu(request.POST)
            if form.is_valid():
                form.save() 
                username=form.cleaned_data.get('username')  
                password=form.cleaned_data.get('password1') 
                user=authenticate(username=username,password=password)
                login(request,user)
                #kayıt olunca kullanıcı oluşturmka için aşağıdaki kısım eklenmeli.
                #yoksa profil update edince hata veriyor.
                current_user=request.user
                data=KullaniciProfili()
                data.user_id=current_user.id
                #default olarak aşağıdaki resim(user.png) profile eklenir.update ile güncellenebilir.
                data.image="images/users/user.png"
                data.save()
                messages.success(request, "Hesabınız başarılı bir şekilde oluşturuldu.")
                return HttpResponseRedirect('/login')
            else:
                messages.warning(request,form.errors)
                return HttpResponseRedirect('/kayitol')
        category=Category.objects.all()    
        form=KullaniciKayitFormu()   
        context ={'category':category,'form':form}
        return render(request,'kayitol.html',context)
    
def logout_view(request):
    logout(request)
    # Çıkış yapıldığında bir sayfaya yönlendirme yapılmalı.Burada ana sayfaya yönlendirdik.
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            current_user=request.user
            kullaniciprofili=KullaniciProfili.objects.get(user_id=current_user.id)
            request.session['userimage'] = kullaniciprofili.image.url
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,"Giriş işlemi Başarısız! Kullanıcı adınızın ve parolanızın doğru olduğundan emin olun.")
            return HttpResponseRedirect('/login')
    category=Category.objects.all()
    context={'category':category}
    return render(request,'login.html',context)


@login_required(login_url='/login') # Kullanıcıının giriş yapıp yapmadığı kontrol edilmeli.
def kullanici_guncelle(request):
    if request.method == 'POST':
        kullanici_formu = KullaniciGuncellemeFormu(request.POST, instance=request.user) # request.user is user  data
        profil_formu = ProfilGuncellemeFormu(request.POST, request.FILES, instance=request.user.kullaniciprofili)
        if kullanici_formu.is_valid() and profil_formu.is_valid():
            kullanici_formu.save()
            profil_formu.save()
            messages.success(request, 'Bilgileriniz başarılı şekilde güncellendi.')
            return HttpResponseRedirect('/user')
    else:
        category = Category.objects.all()
        kullanici_formu = KullaniciGuncellemeFormu(instance=request.user)
        profil_formu = ProfilGuncellemeFormu(instance=request.user.kullaniciprofili) #"userprofile" model -> OneToOneField relatinon with user
        context = {
            'category': category,
            'kullanici_formu': kullanici_formu,
            'profil_formu': profil_formu
                   }
        return render(request, 'kullanici_guncelle.html', context)


@login_required(login_url='/login') # Check login
def kullanici_parola_guncelle(request):
    if request.method == 'POST':
        #PasswordChangeForm zaten django yapsında var.import etmek yeterli.oluşturmak gerekmez.
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!(import etmek gerekiyor.)
            messages.success(request, 'Parolanız başarılı  bir şekilde güncellendi!')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request, 'Hatalı alanları düzeltin.<br>'+ str(form.errors))
            return HttpResponseRedirect('/user/parola')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request, 'kullanici_parola_guncelle.html', {'form': form,'category': category
                       })
        
        
@login_required(login_url='/login') #kullanıcı girişi kontrol ediliyor.
def kullanici_siparisleri(request):
    category = Category.objects.all()
    current_user = request.user
    siparisler=Siparis.objects.filter(user_id=current_user.id)
    sayfaayarlari = SayfaAyarlari.objects.get(pk=1)#sayfaayarlari kısmında pk kaç ise..
    category=Category.objects.all()
    
    alisverissepeti = AlisverisSepeti.objects.filter(user_id=current_user.id)
    favorisepeti = FavoriSepeti.objects.filter(user_id=current_user.id)#ana sayfada favori sepeti
    context = {'category': category,
               'siparisler': siparisler,'sayfaayarlari':sayfaayarlari,
              'alisverissepeti':alisverissepeti,'favorisepeti':favorisepeti,
               }
    return render(request, 'kullanici_siparisleri.html', context)   


@login_required(login_url='/login') # Check login
def kullanici_siparis_urunleri_detayi(request,id):
    category = Category.objects.all()
    current_user = request.user
    siparis = Siparis.objects.get(user_id=current_user.id,id=id)
    siparisurunleri = SiparisUrunu.objects.filter(siparis_id=id)
    context = {
        'category': category,
        'siparis': siparis,
        'siparisurunleri': siparisurunleri,
    }
    #return HttpResponse(context) 
    return render(request, 'kullanici_siparisleri_detayi.html', context)


@login_required(login_url='/login') # Check login
def kullanici_yorumlari(request):
    category = Category.objects.all()
    current_user = request.user
    yorum = Yorumlar.objects.filter(user_id=current_user.id)
    sayfaayarlari = SayfaAyarlari.objects.get(pk=1)#sayfaayarlari kısmında pk kaç ise..
    category=Category.objects.all()
    current_user = request.user  # kullanıcının session bilgileri alınıyor.
    alisverissepeti = AlisverisSepeti.objects.filter(user_id=current_user.id)
    favorisepeti = FavoriSepeti.objects.filter(user_id=current_user.id)#ana sayfada favori sepeti
    #book=Books.objects.all()
    context = {
        'category': category,
        'yorum': yorum,'sayfaayarlari':sayfaayarlari,
              'alisverissepeti':alisverissepeti,'favorisepeti':favorisepeti,
        #'book':book,
    }
    return render(request, 'kullanici_yorumlari.html', context)

@login_required(login_url='/login') # Check login
def yorum_sil(request,id):
   current_user = request.user
   Yorumlar.objects.filter(id=id, user_id=current_user.id).delete()
   messages.success(request, 'Yorum silindi.')
   return HttpResponseRedirect('/user/yorumlar')
