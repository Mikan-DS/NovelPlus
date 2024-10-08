from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.app, name='index'),
    path('users/vk-login/', views.app, name='index'),
    path('users/<int:user_id>/', views.user, name='user'),
    path('about/', views.about, name='about'),
    path('store/', views.store, name='store'),
    path('store/<slug:page>/', views.store, name='store-page'),
    path('vacancy/', views.vacancy, name='vacancy'),
    path('vacancy/<slug:page>/', views.vacancy, name='vacancy-page'),
    path('<slug:collection>/<int:item_id>/', views.item_page, name='item-view'),
    # re_path('(?:store|vacancy|[a-z]+)?(?:/[^/]+)?/?', views.app, name='app'),
]
