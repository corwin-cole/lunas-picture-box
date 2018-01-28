from django.db.models.signals import post_save
from django.db.models import Q
from django.dispatch import receiver
from .models import MainSiteContent


@receiver(post_save, sender=MainSiteContent)
def set_is_live_false_on_other_records(sender, instance, **kwargs):
    """
    When the current `MainSiteContent` is saved with `is_live=True`, updates all other MainSiteContent objects to
    `is_live=False`
    """

    if instance.is_live:
        sender.objects.filter(~Q(pk=instance.pk)).update(is_live=False)
