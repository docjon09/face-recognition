from django.contrib import admin

from .models import ThiefLocation, Person, File

# Register your models here.

admin.site.register(ThiefLocation)
admin.site.register(Person)
admin.site.register(File)