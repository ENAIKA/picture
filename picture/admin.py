from django.contrib import admin
from .models import PhotoImage,Location,Category

# Register your models here.

class PhotoImageAdmin(admin.ModelAdmin):
    filter_horizontal =('location',)

admin.site.register(PhotoImage, PhotoImageAdmin)
admin.site.register(Category)
admin.site.register(Location)