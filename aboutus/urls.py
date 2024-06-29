from django.urls import path
from . import views

urlpatterns = [
    path('about_us/new/', views.about_us_create, name='about_us_create'),
    path('about_us/<int:pk>/edit/', views.about_us_edit, name='about_us_edit'),
    path('', views.about_us, name='about_us')
]