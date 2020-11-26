from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('new/', views.new, name='blog-new'),
]
