from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from book.models import YorumFormu, Yorumlar


# Create your views here.
def index(request):
    text ='merhaba django book'
    context ={'text':text}
    return render (request,'index.html',context)


def addcomment(request,id):
   url = request.META.get('HTTP_REFERER')  # get last url
   #return HttpResponse(url)
   if request.method == 'POST':  # check post
      form = YorumFormu(request.POST)
      if form.is_valid():
         data = Yorumlar()  # create relation with model
         data.konu = form.cleaned_data['konu']
         data.yorum = form.cleaned_data['yorum']
         data.yorum_puani = form.cleaned_data['yorum_puani']
         data.ip = request.META.get('REMOTE_ADDR')
         data.books_id=id
         current_user= request.user
         data.user_id=current_user.id
         data.save()  # save data to table
         messages.success(request, "Yorumunuz başarılı bir şekilde gönderildi...")
         return HttpResponseRedirect(url)

   return HttpResponseRedirect(url)