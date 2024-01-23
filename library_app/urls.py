from django.urls import path
from . import views

app_name = 'library_app'

urlpatterns = [
  path('index/', views.index, name='index'),
  path('', views.register, name='register'),
  path('login/', views.log, name='login'),
  path('create/', views.create_book, name='create_book'),
  path('delete/<int:id>', views.delete, name='delete'),
]