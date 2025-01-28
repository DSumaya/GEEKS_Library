from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
from . import models
from django.views import generic

class SearchView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        return models.Books.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context



# class BookListView(generic.ListView):
#     template_name = 'book.html'
#     context_object_name = 'book_list'
#     model = models.Books
#
#     def get_queryset(self):
#         return self.model.objects.all().order_by('-id')



def book_list(request):
    if request.method == 'GET':
        books_list = models.Books.objects.all().order_by('-id')
        slider = models.Slider.objects.all()
        context = {
            'book_list': books_list,
            'slider': slider
        }
        return render(request, template_name='book.html', context=context)



class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'
    model = models.Books

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Books, id = book_id)

# def book_detail(request, id):
#     if request.method == 'GET':
#         book_id = get_object_or_404(models.Books, id= id)
#         context = {'book_id': book_id}
#         return render(request, template_name= 'book_detail.html', context=context)





class MeView(generic.View):
    def get (self, request):
        return HttpResponse('Hello my name is Sumaya, i am 16 years old 🙃')

# def about_me(request):
#     if request.method == 'GET':
#         return HttpResponse('Hello my name is Sumaya, i am 16 years old 🙃')



class PetsView(generic.View):
    def get (self, request):
        return HttpResponse('I dont have animal) '"<img src = 'https://upload-os-bbs.hoyolab.com/upload/2022/05/14/23130084/b9bdec07c9250c4e390b69ce32059719_5031582172423641290.gif' >")

# def about_my_pets(request):
#     if request.method == 'GET':
#         return HttpResponse('I dont have animal) '"<img src = 'https://upload-os-bbs.hoyolab.com/upload/2022/05/14/23130084/b9bdec07c9250c4e390b69ce32059719_5031582172423641290.gif' >")



class DateTimeView(generic.View):
    def get (self, request):
        time = datetime.datetime.now()
        return HttpResponse(f"{time.strftime('%Y-%m-%d %H:%M:%S')}")


def date_time(request):
    if request.method == 'GET':
        time = datetime.datetime.now()
        return HttpResponse(f"{time.strftime('%Y-%m-%d %H:%M:%S')}")