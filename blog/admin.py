from django.contrib import admin
from .models import GalleryImage, Gallery, Audio, Image, Video, Quote, Link


class GalleryImageInline(admin.StackedInline):
    model = GalleryImage
    extra = 6


class GalleryAdmin(admin.ModelAdmin):
    class Meta:
        model = Gallery

    list_display = [
        'title',
        'date_published',
        'author',
        'category',
        'tags',
    ]

    inlines = [
        GalleryImageInline,
    ]


admin.site.register(Image, admin.ModelAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Video, admin.ModelAdmin)
admin.site.register(Audio, admin.ModelAdmin)
admin.site.register(Quote, admin.ModelAdmin)
admin.site.register(Link, admin.ModelAdmin)
