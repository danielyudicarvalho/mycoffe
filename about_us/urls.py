from django.urls import path
from .views import about_page

app_name = 'about_us'

urlpatterns = [
    path('', about_page, name='about_page'),
]
