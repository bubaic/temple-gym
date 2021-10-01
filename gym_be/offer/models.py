from datetime import datetime, timedelta
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string

from gym.utils import unique_slug_generator


NOW = datetime.now()
NOW_PLUS_60MINS = timedelta(minutes=60) + NOW


class Coupon(models.Model):
    title = models.CharField(max_length=50)
    code = models.CharField(max_length=20, default=get_random_string)
    slug = models.SlugField(blank=True, unique=True)
    valid_from = models.DateTimeField(auto_created=True, default=NOW)
    valid_upto = models.DateTimeField(auto_created=True, default=NOW_PLUS_60MINS)

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Coupon)
def coupon_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, long=12)
