from django.urls import path
from . import views

app_name = 'library_app'

urlpatterns = [
  path('index/', views.index, name='index'),
  path('', views.register, name='register'),
]