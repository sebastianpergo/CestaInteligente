from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name='inicio'),
    path('inicio/', views.inicio, name='inicio'),
    path('shops/', views.shops, name='shops'),
    path('dashboard', views.dashboard, name='dashboard')
]