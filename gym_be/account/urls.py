from django.urls import path, include

from .views import RegisterView, users_list_view


urlpatterns = [
    path('register/', RegisterView.as_view(), name='signup'),
    # function based
    path('users/', users_list_view, name='user-list')
]
