from django.urls import path
from ..views import core_views

app_name = 'core'
urlpatterns = [
    path('', core_views.privacy, name='privacy'),
]
