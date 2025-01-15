from django.contrib import admin

from .models import Tag
from .models import Books

admin.site.register(Tag)
admin.site.register(Books)

