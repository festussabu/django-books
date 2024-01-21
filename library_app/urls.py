from django.urls import path
from . import views

app_name = 'library_app'

urlpatterns = [
  path('', views.index),
  path('signup/', views.sign_up, name='signup'),
  path('login/', views.log_in, name='login'),
]