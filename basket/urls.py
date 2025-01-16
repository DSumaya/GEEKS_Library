from django.urls import path
from. import views

urlpatterns = [
    path('basket_create/', views.basket_create_view, name='basket_create'),
    path('basket_list/', views.basket_list_view, name = 'basket_list'),
    path('basket_list/<int:id>/', views.basket_detail_view, name = 'basket_detail'),
    path('basket_list/<int:id>/update/', views.basket_update_view, name = 'basket_update'),
    path('basket_list/<int:id>/delete/', views.basket_delete_view, name = 'basket_delete'),



]