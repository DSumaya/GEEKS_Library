from crypt import methods

from django.shortcuts import render, redirect, get_object_or_404
from. import  models, forms
from django.views import generic
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache




#creat basket
class BasketCreateView(generic.CreateView):
    template_name = 'basket/basket_create.html'
    form_class = forms.BasketForm
    success_url = '/basket_list/' # аналог redirect

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BasketCreateView, self).form_valid(form=form)

# def basket_create_view(request):
#     if request.method == 'POST':
#         form = forms.BasketForm(request.POST, request.FIELS)
#         if form.is_valid():
#             return redirect('basket_list')
#     else:
#         form = forms.BasketForm
#     return render(request, template_name= 'basket/basket_create.html', context={'form': form})
#




#creat basket list, update, delete
@method_decorator(cache_page(60*15), name = 'dispatch')
class BasketListView(generic.ListView):
    template_name = 'basket/basket_list.html'
    context_object_name = 'basket_list'
    model = models.BasketModel

    def get_queryset(self):
        baskets = cache.get('basket')
        if not baskets:
            baskets = self.model.objects.all().order_by('-id')
            cache.set('baskets', baskets, 60*15)



# def basket_list_view(request):
#     if request.method == 'GET':
#         basket_list = models.BasketModel.objects.all().order_by("-id")
#         context = {'basket_list' : basket_list}
#         return render(request, template_name= 'basket/basket_list.html', context=context)



class BasketDetailView(generic.DetailView):
    template_name = 'basket/basket_detail.html'
    context_object_name = 'basket_id'
    model = models.BasketModel

    def get_object(self, **kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(models.BasketModel, id=basket_id)

# def basket_detail_view(request, id):
#     if request.method == 'GET':
#         basket_id = get_object_or_404(models.BasketModel, id=id )
#         context = {'basket_id': basket_id}
#         return render(request, template_name='basket/basket_detail.html', context=context)



class BasketUpdateView(generic.UpdateView):
    template_name = 'basket/update_basket.html'
    form_class = forms.BasketForm
    success_url = '/basket_id/'

    def get_object(self, **kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(models.BasketModel, id=basket_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BasketUpdateView, self).form_valid(form=form)


# def basket_update_view(request, id):
#     basket_id = get_object_or_404(models.BasketModel, id=id )
#     if request.method == 'POST':
#         form = forms.BasketForm(request.POST, instance=basket_id)
#         if form.is_valid():
#             form.save()
#             return redirect('basket_list')
#     else:
#         form = forms.BasketForm
#         return render(request, template_name='basket/update_basket.html', context={'form': form, 'id': id })



class BasketDeleteView(generic.DeleteView):
    template_name = 'basket/confirm_delete.html'
    success_url = '/basket_list/'
    def get_object(self, **kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(models.BasketModel, id=basket_id)

# def basket_delete_view(request, id):
#     basket_id = get_object_or_404(models.BasketModel, id=id)
#     basket_id.delete()
#     return redirect('basket_list')






