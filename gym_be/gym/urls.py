from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import index, api_list

urlpatterns = [
	path('', index, name='homepage'),
	# path('home/', index, name='homepage'),
	path('accounts/', include('account.urls')),
	path('admin/', admin.site.urls),

	path('api-list/', api_list),
	
	# custom `djoser` urls
	path('api/v1/', include('djoser.urls')),
	path('api/v1/', include('djoser.urls.authtoken')),

	# application specific urls
	path('api/v1/', include('feedback.urls')),
	path('api/v1/', include('product.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
