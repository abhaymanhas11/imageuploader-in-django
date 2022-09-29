from django.contrib import admin
from .models import imageuploader

@admin.register(imageuploader)
class imageadmin(admin.ModelAdmin):
    list_display = ['id','image']

