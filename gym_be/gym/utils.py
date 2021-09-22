import random
import string
import os

from django.utils.crypto import get_random_string
from django.utils.text import slugify


def unique_slug_generator(instance, new_slug=None, long=None):
    '''Generates random slugs'''
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = f'{slug}-{get_random_string(length=long)}'
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def get_image_path(instance, file):
    "Returns image path according to uploads to model"
    Klass = instance.__class__._meta
    folder = Klass.verbose_name_plural.replace(' ', '_')
    _, ext = os.path.splitext(os.path.basename(file))
    name = f'{get_random_string(length=6)}{ext}'
    return f'{folder}/{name}'
