from django.urls import path
from . import views

urlpatterns = [
    path('banners/', views.banner_list, name='banner_list'),
    path('banners/<int:pk>/', views.banner_detail, name='banner_detail'),
    path('banners/create/', views.banner_create, name='banner_create'),
    path('banners/<int:pk>/update/', views.banner_update, name='banner_update'),
    path('banners/<int:pk>/delete/', views.banner_delete, name='banner_delete'),
]
