from django.urls import path
from . import views

app_name = 'champion'
urlpatterns = [
    path('', views.champion_list, name='champion_list'),
    path('<champion_name>', views.champion, name='champion')
]
