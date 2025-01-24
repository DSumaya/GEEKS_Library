from  django.urls import path
from . import  views

urlpatterns = [
    path('library_list/', views.LibraryListviews.as_view(), name = 'library_list'),
    path('library_form/', views.LibraryFormView.as_view(), name = 'library_form'),
]
