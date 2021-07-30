from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class UserProfile(models.Model):
	user = models.OneToOneField(User, verbose_name='username', on_delete=models.CASCADE)
	first_name = models.CharField(verbose_name='first name', max_length=25, default='firstname')
	last_name = models.CharField(verbose_name='last name', max_length=25, default='lastname')

	def __str__(self):
		return f'{self.first_name} {self.last_name}'
