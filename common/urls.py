from django.urls import path

from . import views

urlpatterns = [
    path('get-collection/<str:variant>/<str:collection>', views.get_cards, name='get-collection'),
    path('get-item/<str:collection>/<int:item_id>', views.get_item, name='get-collection'),
    path('update/item/', views.update_item, name='update-item'),
    path('get/available-context-buttons/', views.context_buttons_list, name='available-context-buttons'),
    path('get/available-item-statuses/', views.item_statuses_list, name='available-item-statuses'),
    path('get/comments/<int:item_id>/', views.get_item_comments, name='get-comments'),
    path('add/comments/<int:item_id>/', views.add_item_comment, name='add-comment'),
]
