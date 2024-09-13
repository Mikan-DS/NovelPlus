from django.urls import path

from . import views

urlpatterns = [
    path('get-me/', views.get_me, name='get-me'),
]
