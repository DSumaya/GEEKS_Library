from django.urls import path
from . import views


urlpatterns = [
    path('all_books/', views.BookAllView.as_view(), name= 'all_books'),
    path('all_tale/',views.BookTaleViews.as_view(), name='all_tale'),
    path('all_fantasy/', views.BookFantasyViews.as_view(), name='all_fantasy'),
    path('all_drama/', views.BookDramaViews.as_view(), name='all_drama'),
]