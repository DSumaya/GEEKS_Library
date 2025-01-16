
from django.shortcuts import render, redirect, get_object_or_404
from. import  models, forms
from .models import BasketModel


#creat basket_list

def basket_create_view(request):
    if request.method == 'POST':
        form = forms.BasketForm(request.POST, request.FIELS)
        if form.is_valid():
            return redirect('basket_list')
    else:
        form = forms.BasketForm
    return render(request, template_name= 'basket/basket_create.html', context={'form': form})

#creat basket_list detail
def basket_list_view(request):
    if request.method == 'GET':
        basket_list = models.BasketModel.objects.all().order_by("-id")
        context = {'basket_list' : basket_list}
        return render(request, template_name= 'basket/basket_list.html', context=context)


def basket_detail_view(request, id):
    if request.method == 'GET':
        basket_id = get_object_or_404(models.BasketModel, id=id )
        context = {'basket_id': basket_id}
        return render(request, template_name='basket/basket_detail.html', context=context)

def basket_update_view(request, id):
    basket_id = get_object_or_404(models.BasketModel, id=id )
    if request.method == 'POST':
        form = forms.BasketForm(request.POST, instance=basket_id)
        if form.is_valid():
            form.save()
            return redirect('basket_list')
    else:
        form = forms.BasketForm
        return render(request, template_name='basket/update_basket.html', context={'form': form, 'id': id })


def basket_delete_view(request, id):
    basket_id = get_object_or_404(models.BasketModel, id=id)
    basket_id.delete()
    return redirect('basket_list')








