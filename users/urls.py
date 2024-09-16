from django.urls import path

from . import views

urlpatterns = [
    path('get-me/', views.get_me, name='get-me'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
]
