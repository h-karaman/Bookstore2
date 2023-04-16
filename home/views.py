from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

from home.models import SayfaAyarlari

# Create your views here.
def index(request):
    sayfaayarlari = SayfaAyarlari.objects.get(pk=4)
    context ={'setting':sayfaayarlari}
    return render (request,'index.html',context)
