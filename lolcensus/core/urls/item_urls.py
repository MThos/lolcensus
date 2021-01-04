from django.urls import path
from ..views import item_views

app_name = 'core'
urlpatterns = [
    path('', item_views.item_list, name='item_list'),
    path('<item_id>', item_views.item, name='item'),
]
