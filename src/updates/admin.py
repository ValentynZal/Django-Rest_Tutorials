from django.contrib import admin

from .models import Update as UpdateModel


class UpdateModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content', 'image') 

admin.site.register(UpdateModel, UpdateModelAdmin)
