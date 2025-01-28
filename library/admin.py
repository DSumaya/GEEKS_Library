from django.contrib import admin
from . import models
from .models import Slider, Books, Comment





admin.site.register(Slider)


admin.site.register(Books)
admin.site.register(Comment)

# Register your models here.