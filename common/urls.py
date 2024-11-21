from django.urls import path

from . import views

urlpatterns = [
    path('get-collection/<str:variant>/<str:collection>', views.get_cards, name='get-collection'),
    path('get-item/<str:collection>/<int:item_id>', views.get_item, name='get-collection'),
    path('update/item/', views.update_item, name='update-item'),
]
