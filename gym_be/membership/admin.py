from django.contrib import admin

from .models import Group, Plan

admin.site.register([Group, Plan])