from django.contrib import admin
from .models import Books, Comment

admin.site.register(Books)
admin.site.register(Comment)

# Register your models here.