from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import index

urlpatterns = [
	path('', index, name='homepage'),
	# path('home/', index, name='homepage'),
	path('admin/', admin.site.urls),
	path('accounts/', include('account.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
