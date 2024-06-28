from django import forms
from .models import SubscriptionPlan

class SubscriptionPlanForm(forms.ModelForm):
    class Meta:
        model = SubscriptionPlan
        fields = ['name', 'price_monthly', 'price_annual', 'description', 'images', 'is_active']
