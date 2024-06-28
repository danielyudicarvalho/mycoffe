from django.db import models
from django.contrib.auth.models import User

class SubscriptionPlan(models.Model):
    PLAN_TYPE_CHOICES = [
        ('monthly', 'Monthly'),
        ('annual', 'Annual'),
    ]
    
    name = models.CharField(max_length=255)
    price_monthly = models.DecimalField(max_digits=10, decimal_places=2)
    price_annual = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    images = models.ImageField(upload_to='plan_images/')
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.plan.name}"
