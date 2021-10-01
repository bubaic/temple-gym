from datetime import datetime, timedelta
from django.db import models
from django.db.models import CASCADE
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from gym.utils import unique_slug_generator, get_random_string

DAYS30 = timedelta(days=30) + datetime.now()
GROUPS = [
    ('PERSONAL', 'personal'),
    ('MULTIPLE', 'multiple'),
]


class Group(models.Model):
    title = models.CharField(_("Group name"), max_length=50)
    kind = models.CharField(max_length=50, choices=GROUPS)

    def __str__(self):
        return self.title


class Plan(models.Model):
    member_group = models.ForeignKey(Group, on_delete=CASCADE, related_name='plan')
    title = models.CharField(_("Plan name"), max_length=50, blank=True, default='')
    slug = models.SlugField(blank=True, unique=True, default=get_random_string)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    has_referal = models.BooleanField(default=False)
    validity = models.DateTimeField(auto_created=True, default=DAYS30)

    def __str__(self):
        return self.slug

    # def set_referral_bonus(self):
    #     self.has_referal = True


@receiver(pre_save, sender=Plan)
def membership_plan_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, long=8)

