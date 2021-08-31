from django.urls import path, include
from rest_framework import routers

from .views import RegisterView, \
	users_list_view
	# UserListView
#
# router = routers.DefaultRouter()
# router.register(r'users', UserListView, basename='user-list')

urlpatterns = [
	path('register/', RegisterView.as_view(), name='signup'),
	# path('', include(router.urls)),

	# function based
	path('users/', users_list_view, name='user-list')
]
