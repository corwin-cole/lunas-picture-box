from django.contrib import admin
from .models import Photo, Category


admin.site.register(Category, admin.ModelAdmin)
admin.site.register(Photo, admin.ModelAdmin)
