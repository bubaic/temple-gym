from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'first_name', 'last_name', )

	class Meta:
		model = UserProfile


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.unregister(Group)
