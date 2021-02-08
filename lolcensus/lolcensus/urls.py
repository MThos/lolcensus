from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('champion/', include('core.urls.champion_urls')),
    path('item/', include('core.urls.item_urls')),
    path('terms/', include('core.urls.terms_urls')),
    path('privacy/', include('core.urls.privacy_urls')),
    path('cookies/', include('core.urls.cookies_urls')),
    path('status/', include('core.urls.status_urls')),
    path('admin/', admin.site.urls),
]
