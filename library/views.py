from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
from . import models

def book_list(request):
    if request.method == 'GET':
        books_list = models.Books.objects.all().order_by('-id')
        context = {'book_list': books_list}
        return render(request, template_name='book.html', context=context)


def book_detail(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Books, id= id)
        context = {'book_id': book_id}
        return render(request, template_name= 'book_detail.html', context=context)







def about_me(request):
    if request.method == 'GET':
        return HttpResponse('Hello my name is Sumaya, i am 16 years old 🙃')


def about_my_pets(request):
    if request.method == 'GET':
        return HttpResponse('I dont have animal) '"<img src = 'https://upload-os-bbs.hoyolab.com/upload/2022/05/14/23130084/b9bdec07c9250c4e390b69ce32059719_5031582172423641290.gif' >")

def date_time(request):
    if request.method == 'GET':
        time = datetime.datetime.now()
        return HttpResponse(f"{time.strftime('%Y-%m-%d %H:%M:%S')}")