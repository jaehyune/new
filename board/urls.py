from django.urls import path
from . import views

urlpatterns = [
        path('', views.board, name='board'),
        path('new/', views.new, name='new'),
        path('create/', views.create, name='create'),
        path('<int:board_id>/', views.detail, name='detail'),
]