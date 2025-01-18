from django.shortcuts import render
from django.template.context_processors import request

from .import models
from django.views import generic

#all
class BookAllView(generic.ListView):
    template_name = 'hashtags/all_books.html'
    context_object_name = 'all_books'
    model = models.Books

    def get_queryset(self):
        return self.model.objects.all()

# def all_books(request):
#     if request.method == 'GET':
#         all_books = models.Books.objects.all()
#         context = {'all_books' : all_books}
#         return render(request, template_name='hashtags/all_books.html', context= context)


class BookTaleViews(generic.ListView):
    template_name = 'hashtags/all_tale.html'
    context_object_name = 'all_tale'
    model = models.Books

    def get_queryset(self):
        return self.model.objects.filter(tags__name='Сказки')

# def all_tale(request):
#     if request.method == 'GET':
#         all_tale = models.Books.objects.filter(tags__name='Сказки')
#         context = {'all_tale' : all_tale}
#         return render(request, template_name='hashtags/all_tale.html', context=context)



class BookFantasyViews(generic.ListView):
    template_name = 'hashtags/all_fantasy.html'
    context_object_name = 'all_fantasy'
    model = models.Books

    def get_queryset(self):
        return self.model.objects.filter(tags__name='Фантастика')

# def all_fantasy(request):
#     if request.method == 'GET':
#         all_fantasy = models.Books.objects.filter(tags__name='Фантастика')
#         context = {'all_fantasy' : all_fantasy}
#         return render(request, template_name='hashtags/all_fantasy.html', context=context)



class BookDramaViews(generic.ListView):
    template_name = 'hashtags/all_drama.html'
    context_object_name = 'all_drama'
    model = models.Books

    def get_queryset(self):
        return self.model.objects.filter(tags__name='Драма')

# def all_drama(request):
#     if request.method == 'GET':
#         all_drama = models.Books.objects.filter(tags__name='Драма')
#         context = {'all_drama' : all_drama}
#         return render(request, template_name='hashtags/all_drama.html', context=context)