from django.http import HttpResponse

from . import  models, forms
from django.views import generic


class LibraryListviews(generic.ListView):
    template_name = 'parser/library_list.html'
    context_object_name = 'library'
    model =models.LibraryParser

    def get_queryset(self):
        return self.model.objects.all()


class LibraryFormView(generic.FormView):
    template_name = 'parser/library_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return  HttpResponse('Парсинг успешно завершен')
        else:
            return super(LibraryFormView, self).post(request, *args, **kwargs)




