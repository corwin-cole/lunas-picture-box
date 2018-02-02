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
        on_delete=models.CASCADE,
        null=True
    )

    # Video field
    video_url = models.URLField(
        verbose_name='Video URL',
        help_text='Add the URL of a video on your YouTube account',
        null=True
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
        related_name='background_image',
        null=True
    )

    # Link fields; background_image is used for Links also
    link = models.URLField(help_text='Enter the link URL')
    link_text = models.CharField(
        max_length=200,
        help_text='Clickable text'
    )
    attribution = models.CharField(
        max_length=50,
        help_text='Similar to a byline, follows the clickable text'
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date_published',)


class Image(BlogPost):
    def __str__(self):
        return '{title} (image: {image__title})'.format(
            title=self.title,
            image__title=self.image.title
        )

    class Meta:
        proxy = True


class Video(BlogPost):
    def __str__(self):
        return '{title} ({video_url})'.format(
            title=self.title,
            video_url=self.video_url
        )

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
    image = models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE,
        null=True
    )


class Audio(BlogPost):
    class Meta:
        verbose_name_plural = 'Audio'
        proxy = True


class Quote(BlogPost):
    def __str__(self):
        return '{title} ({quote} by: {by})'.format(
            title=self.title,
            quote=self.quote,
            by=self.by
        )

    class Meta:
        proxy = True


class Link(BlogPost):
    def __str__(self):
        return '{title} (link text: {link_text})'.format(
            title=self.title,
            link_text=self.link_text
        )

    class Meta:
        proxy = True
