from django.urls import path
from . import views

urlpatterns = [
    path('', views.artist_list, name='artist_list'),
    path('<int:pk>/', views.artist_detail, name='artist_detail'),
    path('create/', views.artist_create, name='artist_create'),
    path('<int:pk>/update/', views.artist_update, name='artist_update'),
    path('<int:pk>/delete/', views.artist_delete, name='artist_delete'),
]