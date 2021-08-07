from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


class UserManager(BaseUserManager):
	def create_user(self, email, username, password=None, is_active=True, is_staff=False, is_admin=False):
		if not email:
			raise TypeError("Email can't be left blank")
		if not username:
			raise TypeError("Username can't be left blank")
		if password is None:
			raise TypeError("Password should've at-least 6 characters")

		user_obj = self.model(email=self.normalize_email(email), username=username)
		user_obj.set_password(password)
		user_obj.staff = is_staff
		user_obj.admin = is_admin
		user_obj.save()
		return user_obj

	def create_superuser(self, email, username, password):
		user = self.create_user(email, username, password, is_staff=True, is_admin=True)
		return user

	def create_staffuser(self, email, username, password):
		user = self.create_user(email, username, password, is_staff=True)
		return user


class User(AbstractBaseUser):
	email = models.EmailField(verbose_name='Email Address', max_length=255, unique=True, db_index=True)
	username = models.CharField(verbose_name='Username', max_length=255, unique=True, db_index=True)
	is_verified = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	staff = models.BooleanField(default=False)
	admin = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	objects = UserManager()

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.staff

	@property
	def is_admin(self):
		return self.admin

	@property
	def tokens(self):
		return ''


class Guest(models.Model):
	email = models.EmailField(verbose_name='Email Address', max_length=255, unique=True, db_index=True)
	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.email


# ---- Obsolete code  -----

"""
class UserProfile(models.Model):
	user = models.OneToOneField(User, verbose_name='username', on_delete=models.CASCADE)
	first_name = models.CharField(verbose_name='first name', max_length=25, default='firstname')
	last_name = models.CharField(verbose_name='last name', max_length=25, default='lastname')

	def __str__(self):
		return f'{self.first_name} {self.last_name}'
"""
