from django.urls import path
from . import views
#from .views import date_time

urlpatterns = [
    path('', views.BookListView.as_view(), name = 'book_list'),
    path('book_detail/<int:id>/', views.BookDetailView.as_view(), name='book_detail'),
    path('about_me/', views.MeView.as_view(), name= 'about_me'),
    path('about_my_pets/', views.PetsView.as_view(), name= 'about_my_pets'),
    path('date_time/', views.DateTimeView.as_view(), name= 'date_time'),
    path('search/', views.SearchView.as_view(), name= 'search')
]


