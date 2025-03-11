from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Главная страница
    path('create/', views.create_post, name='create_post'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('responses/', views.response_list, name='response_list'),
    path('add_response/<int:pk>/', views.add_response, name='add_response'),
    path('accept_response/<int:pk>/', views.accept_response, name='accept_response'),
    path('delete_response/<int:pk>/', views.delete_response, name='delete_response'),
]