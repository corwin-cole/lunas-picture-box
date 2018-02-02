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
    """
    Allows a gallery plus its child gallery images to be managed concurrently
    """
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

    class Meta:
        model = Gallery


class ImageAdmin(admin.ModelAdmin):
    """
    Image post admin; base blog post fields with a single image
    """
    fields = BLOG_POST_BASE_FIELDS + ['image']

    class Meta:
        model = Image


class VideoAdmin(admin.ModelAdmin):
    """
    Video post admin; base blog post fields with a single video URL
    """
    fields = BLOG_POST_BASE_FIELDS + ['video_url']

    class Meta:
        model = Video


class AudioAdmin(admin.ModelAdmin):
    """
    Audio post admin; base blog post fields with a single audio file and background image
    """
    fields = BLOG_POST_BASE_FIELDS + [
        'audio_file',
        'background_image'
    ]

    class Meta:
        model = Audio


class LinkAdmin(admin.ModelAdmin):
    """
    Link post admin; base blog post fields with a link, clickable text, attribution, and background image
    """
    fields = BLOG_POST_BASE_FIELDS + [
        'link',
        'link_text',
        'attribution',
        'background_image'
    ]

    class Meta:
        model = Link


class QuoteAdmin(admin.ModelAdmin):
    """
    Quote post admin; base blog post fields with a quote, attribution, and background image
    """
    fields = BLOG_POST_BASE_FIELDS + [
        'quote',
        'by',
        'background_image'
    ]

    class Meta:
        model = Quote


admin.site.register(Image, ImageAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Audio, AudioAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Link, LinkAdmin)
