from django.contrib import admin
from .models import PhotoImage,Location,Category

# Register your models here.


admin.site.register(PhotoImage)
admin.site.register(Category)
admin.site.register(Location)