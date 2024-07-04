from django.urls import path
from . import views

app_name = 'subscription'  # Define the namespace

urlpatterns = [
    path('plans/', views.subscription_plans, name='plans'),  # Ensure this is named 'plans'
    path('subscribe/<int:plan_id>/', views.subscribe, name='subscribe'),
    path('my-subscriptions/', views.user_subscriptions, name='my-subscriptions'),
]
