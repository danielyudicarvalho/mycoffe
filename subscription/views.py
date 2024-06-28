from django.shortcuts import render, redirect, get_object_or_404
from .models import SubscriptionPlan, UserSubscription
from django.contrib.auth.decorators import login_required

@login_required
def subscription_plans(request):
    plans = SubscriptionPlan.objects.filter(is_active=True)
    return render(request, 'subscription/plans.html', {'plans': plans})

@login_required
def subscribe(request, plan_id):
    plan = get_object_or_404(SubscriptionPlan, id=plan_id)
    if request.method == 'POST':
        UserSubscription.objects.create(user=request.user, plan=plan)
        return redirect('user_subscriptions')
    return render(request, 'subscription/subscribe.html', {'plan': plan})

@login_required
def user_subscriptions(request):
    subscriptions = UserSubscription.objects.filter(user=request.user)
    return render(request, 'subscription/user_subscription.html', {'subscriptions': subscriptions})
