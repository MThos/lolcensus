import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('champion/', include('core.urls.champion_urls')),
    path('item/', include('core.urls.item_urls')),
    path('terms/', include('core.urls.terms_urls')),
    path('privacy/', include('core.urls.privacy_urls')),
    path('cookies/', include('core.urls.cookies_urls')),
    path('contact/', include('core.urls.contact_urls')),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('sitemap.xml', TemplateView.as_view(template_name='sitemap.xml', content_type='text/xml')),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
]
