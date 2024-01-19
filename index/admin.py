from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(genre)
admin.site.register(person)
admin.site.register(film)
admin.site.register(lang)