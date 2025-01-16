from django.urls import path
from . import views


urlpatterns = [
    path('all_books/', views.all_books, name= 'all_books'),
    path('all_tale/',views.all_tale, name='all_tale'),
    path('all_fantasy/', views.all_fantasy, name='all_fantasy'),
    path('all_drama/', views.all_drama, name='all_drama'),
]