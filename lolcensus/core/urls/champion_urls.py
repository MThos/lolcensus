from django.urls import path
from ..views import champion_views

app_name = 'core'
urlpatterns = [
    path('', champion_views.champion_list, name='champion_list'),
    path('<champion_name>', champion_views.champion, name='champion'),
]
