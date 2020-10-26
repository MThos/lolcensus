from django.urls import path
from .views import *

app_name = 'champion'
urlpatterns = [
    path('', ChampionList.as_view(), name='champion'),
]
