from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User, Guest


class UserAdmin(admin.ModelAdmin):
	list_display = ('email', 'username', 'admin', 'staff')
	fieldsets = (
		('Main', {'fields': ('username', 'email', 'password')}),
		('Permissions', {'fields': ('admin', 'staff', 'is_active')}),
	)
	search_fields = ('email', 'username')

	class Meta:
		model = User


class GuestAdmin(admin.ModelAdmin):
	search_fields = ('email', 'first_name', 'last_name')

	class Meta:
		model = Guest


admin.site.register(User, UserAdmin)
admin.site.register(Guest, GuestAdmin)
admin.site.unregister(Group)
