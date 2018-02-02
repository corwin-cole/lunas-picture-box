from django.contrib import admin
from django.db.models import Q
from .models import GalleryImage, Gallery, Audio, Image, Video, Quote, Link


BLOG_POST_BASE_FIELDS = [
    'author',
    'date_published',
    'title',
    'description',
    'category',
    'body'
]

BLOG_POST_BASE_LIST_DISPLAY = [
    'title',
    'date_published',
    'author',
    'category',
    'tag_list'
]


class TaggedModelAdmin(admin.ModelAdmin):
    """
    Allows tags in admin list display
    """
    @staticmethod
    def tag_list(obj):
        return ', '.join(tag.name for tag in obj.tags.all())


class GalleryImageInline(admin.StackedInline):
    model = GalleryImage
    extra = 6


class GalleryAdmin(TaggedModelAdmin):
    """
    Allows a gallery plus its child gallery images to be managed concurrently
    """
    fields = BLOG_POST_BASE_FIELDS

    list_display = BLOG_POST_BASE_LIST_DISPLAY

    inlines = [
        GalleryImageInline,
    ]

    def get_queryset(self, request):
        gallery_ids = GalleryImage.objects.all().values_list('gallery_id', flat=True)
        return self.model.objects.filter(id__in=list(set(gallery_ids)))

    class Meta:
        model = Gallery


class ImageAdmin(TaggedModelAdmin):
    """
    Image post admin; base blog post fields with a single image
    """
    fields = BLOG_POST_BASE_FIELDS + ['image']

    list_display = BLOG_POST_BASE_LIST_DISPLAY + ['get_image_title']

    def get_queryset(self, request):
        return self.model.objects.exclude(image=None)

    def get_image_title(self, obj):
        return obj.image.title
    get_image_title.admin_order_field = 'image__title'
    get_image_title.short_description = 'Image Title'

    class Meta:
        model = Image


class VideoAdmin(TaggedModelAdmin):
    """
    Video post admin; base blog post fields with a single video URL
    """
    fields = BLOG_POST_BASE_FIELDS + ['video_url']

    list_display = BLOG_POST_BASE_LIST_DISPLAY + ['video_url']

    def get_queryset(self, request):
        return self.model.objects.exclude(Q(video_url=None) | Q(video_url=''))

    class Meta:
        model = Video


class AudioAdmin(TaggedModelAdmin):
    """
    Audio post admin; base blog post fields with a single audio file and background image
    """
    fields = BLOG_POST_BASE_FIELDS + [
        'audio_file',
        'background_image'
    ]

    list_display = BLOG_POST_BASE_LIST_DISPLAY

    def get_queryset(self, request):
        return self.model.objects.exclude(audio_file='')

    class Meta:
        model = Audio


class LinkAdmin(TaggedModelAdmin):
    """
    Link post admin; base blog post fields with a link, clickable text, attribution, and background image
    """
    fields = BLOG_POST_BASE_FIELDS + [
        'link',
        'link_text',
        'attribution',
        'background_image'
    ]

    list_display = BLOG_POST_BASE_LIST_DISPLAY + ['link_text']

    def get_queryset(self, request):
        return self.model.objects.exclude(link='')

    class Meta:
        model = Link


class QuoteAdmin(TaggedModelAdmin):
    """
    Quote post admin; base blog post fields with a quote, attribution, and background image
    """
    fields = BLOG_POST_BASE_FIELDS + [
        'quote',
        'by',
        'background_image'
    ]

    list_display = BLOG_POST_BASE_LIST_DISPLAY + ['by']

    def get_queryset(self, request):
        return self.model.objects.exclude(quote='')

    class Meta:
        model = Quote


admin.site.register(Image, ImageAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Audio, AudioAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Link, LinkAdmin)
