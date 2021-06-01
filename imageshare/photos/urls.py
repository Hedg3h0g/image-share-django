from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('upload/', views.addPhoto, name='add'),
    path('<str:pk>', views.delPhoto, name='del'),
]