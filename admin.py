from django.contrib import admin

from images.models import Image


# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title','slug','created']
    list_filter = ['created']


