from django.contrib import admin
from .models import GalleryImage, Gallery, Audio, Image, Video, Quote, Link


BLOG_POST_BASE_FIELDS = [
    'author',
    'date_published',
    'title',
    'description',
    'category',
    'body'
]


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


class ImageAdmin(admin.ModelAdmin):
    class Meta:
        model = Image

    fields = BLOG_POST_BASE_FIELDS + ['image']


class VideoAdmin(admin.ModelAdmin):
    class Meta:
        model = Video

    fields = BLOG_POST_BASE_FIELDS + ['video_url']


class AudioAdmin(admin.ModelAdmin):
    class Meta:
        model = Audio

    fields = BLOG_POST_BASE_FIELDS + ['audio_file']


class LinkAdmin(admin.ModelAdmin):
    class Meta:
        model = Link

    fields = BLOG_POST_BASE_FIELDS + [
        'link',
        'background_image'
    ]


class QuoteAdmin(admin.ModelAdmin):
    class Meta:
        model = Quote

    fields = BLOG_POST_BASE_FIELDS + [
        'quote',
        'by',
        'background_image'
    ]


admin.site.register(Image, ImageAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Audio, AudioAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Link, LinkAdmin)
