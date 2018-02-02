from django.db import models
from django.contrib.auth import get_user_model
from photos.models import Photo, Category, UUIDTaggedItem, TaggableManager
from ckeditor.fields import RichTextField
import uuid


class BlogPost(models.Model):
    """
    Parent class for proxies describing various types of blog posts
    """

    # Base fields
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    author = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE
    )
    date_published = models.DateField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    tags = TaggableManager(
        through=UUIDTaggedItem,
        help_text='Separate by commas. "Use quotes" for multi-word tags',
        blank=True
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE
    )
    body = RichTextField()

    # Image field
    image = models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE
    )

    # Video field
    video_url = models.FileField(
        verbose_name='Video URL',
        help_text='Add the URL of a video on your YouTube account'
    )

    # Audio field
    audio_file = models.FileField()

    # Quote fields
    quote = models.CharField(
        max_length=1000,
        help_text='1000 characters max'
    )
    by = models.CharField(
        max_length=100,
        help_text='100 characters max'
    )
    background_image = models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE,
        related_name='background_image'
    )

    # Link field; background_image is used for Links also
    link = models.URLField()

    class Meta:
        ordering = ('-date_published',)


class Image(BlogPost):
    class Meta:
        proxy = True


class Video(BlogPost):
    class Meta:
        proxy = True


class Gallery(BlogPost):
    class Meta:
        verbose_name_plural = 'Galleries'
        proxy = True


class GalleryImage(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    gallery = models.ForeignKey(
        to=Gallery,
        on_delete=models.CASCADE
    )


class Audio(BlogPost):
    class Meta:
        verbose_name_plural = 'Audio'
        proxy = True


class Quote(BlogPost):
    class Meta:
        proxy = True


class Link(BlogPost):
    class Meta:
        proxy = True
