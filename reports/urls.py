from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    # Other URL patterns
    path('', views.product_report, name='product_report'),
    path('report/products/<str:format>/', views.product_report, name='product_report_format'),
    path('report/sales/', views.sales_report, name='sales_report'),
    path('report/sales/<str:format>/', views.sales_report, name='sales_report_format'),
    path('report/subscriptions/', views.subscription_report, name='subscription_report'),
    path('report/subscriptions/<str:format>/', views.subscription_report, name='subscription_report_format'),
]
