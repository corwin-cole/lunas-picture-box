from django.db import models
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase
import uuid


class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    """
    Base class for tags applied to models that have UUID primary keys
    """

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Category(models.Model):
    """
    Categories, for organizing photos
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        max_length=50,
        help_text='Category name. Maximum 50 characters'
    )
    is_live = models.BooleanField(
        default=False,
        help_text='Check this when the category is ready to go live'
    )
    cover_image = models.ImageField(
        null=True,
        blank=True
    )
    portfolio_header = models.CharField(
        max_length=100,
        help_text='A header for carousels of photos within this category',
        blank=True
    )
    portfolio_body = models.TextField(
        help_text='Body for carousels of photos within this category. Can be multi-paragraph',
        blank=True
    )

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('-is_live', 'name',)

    def __str__(self):
        return self.name or 'UNNAMED'

    @property
    def filter_name(self):
        return self.name.split(' ')[0].lower()


class Photo(models.Model):
    """
    Photos, for showcase and sale
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    image = models.ImageField()
    is_live = models.BooleanField(
        default=False,
        help_text='Check this when the image is ready to go live'
    )
    title = models.CharField(
        max_length=200,
        help_text='Max 200 characters',
        blank=True
    )
    heading = models.CharField(
        max_length=1000,
        help_text='First heading. Max 1000 characters.',
        blank=True
    )
    subheading = models.CharField(
        max_length=1000,
        help_text='Second heading. Max 1000 characters.',
        blank=True
    )
    customers_can_buy_prints = models.BooleanField(
        default=False,
        help_text='Check this when prints are available for purchase'
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET_NULL,
        help_text='Choose a category or leave blank',
        null=True,
        blank=True
    )
    tags = TaggableManager(
        through=UUIDTaggedItem,
        help_text='Separate by commas. "Use quotes" for multi-word tags',
        blank=True
    )

    def __str__(self):
        return self.title or 'UNTITLED'
