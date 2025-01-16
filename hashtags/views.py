from django.shortcuts import render

from .import models

#all
def all_books(request):
    if request.method == 'GET':
        all_books = models.Books.objects.all()
        context = {'all_books' : all_books}
        return render(request, template_name='hashtags/all_books.html', context= context)




def all_tale(request):
    if request.method == 'GET':
        all_tale = models.Books.objects.filter(tags__name='Сказки')
        context = {'all_tale' : all_tale}
        return render(request, template_name='hashtags/all_tale.html', context=context)


def all_fantasy(request):
    if request.method == 'GET':
        all_fantasy = models.Books.objects.filter(tags__name='Фантастика')
        context = {'all_fantasy' : all_fantasy}
        return render(request, template_name='hashtags/all_fantasy.html', context=context)


def all_drama(request):
    if request.method == 'GET':
        all_drama = models.Books.objects.filter(tags__name='Драма')
        context = {'all_drama' : all_drama}
        return render(request, template_name='hashtags/all_drama.html', context=context)