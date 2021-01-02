from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('champion/', include('core.urls.champion_urls')),
    path('item/', include('core.urls.item_urls')),
    path('admin/', admin.site.urls),
]
