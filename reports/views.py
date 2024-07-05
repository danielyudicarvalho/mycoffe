import csv
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from item.models import Item, OrderItem, Order
from subscription.models import SubscriptionPlan, UserSubscription
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

@login_required
def product_report(request, format=None):
    items = Item.objects.all()
    if format == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="product_report.csv"'

        writer = csv.writer(response)
        writer.writerow(['ID', 'Name', 'Description', 'Price', 'Category', 'Created By', 'Created At'])
        for item in items:
            writer.writerow([item.id, item.name, item.description, item.price, item.category.name, item.created_by.username, item.created_at])

        return response
    elif format == 'pdf':
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="product_report.pdf"'
        c = canvas.Canvas(response, pagesize=letter)
        c.drawString(100, 750, "Product Report")
        y = 700
        for item in items:
            c.drawString(100, y, f"{item.id} - {item.name} - {item.description} - {item.price} - {item.category.name} - {item.created_by.username} - {item.created_at}")
            y -= 20
        c.showPage()
        c.save()
        return response
    return render(request, 'reports/product_report.html', {'items': items})

@login_required
def sales_report(request, format=None):
    orders = Order.objects.all()
    if format == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="sales_report.csv"'

        writer = csv.writer(response)
        writer.writerow(['Order ID', 'User', 'Total Price', 'Created At'])
        for order in orders:
            writer.writerow([order.id, order.user.username, order.total_price, order.created_at])

        return response
    elif format == 'pdf':
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="sales_report.pdf"'
        c = canvas.Canvas(response, pagesize=letter)
        c.drawString(100, 750, "Sales Report")
        y = 700
        for order in orders:
            c.drawString(100, y, f"{order.id} - {order.user.username} - {order.total_price} - {order.created_at}")
            y -= 20
        c.showPage()
        c.save()
        return response
    return render(request, 'reports/sales_report.html', {'orders': orders})

@login_required
def subscription_report(request, format=None):
    subscriptions = UserSubscription.objects.all()
    if format == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="subscription_report.csv"'

        writer = csv.writer(response)
        writer.writerow(['ID', 'User', 'Plan', 'Start Date', 'End Date', 'Is Active'])
        for sub in subscriptions:
            writer.writerow([sub.id, sub.user.username, sub.plan.name, sub.start_date, sub.end_date, sub.is_active])

        return response
    elif format == 'pdf':
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="subscription_report.pdf"'
        c = canvas.Canvas(response, pagesize=letter)
        c.drawString(100, 750, "Subscription Report")
        y = 700
        for sub in subscriptions:
            c.drawString(100, y, f"{sub.id} - {sub.user.username} - {sub.plan.name} - {sub.start_date} - {sub.end_date} - {sub.is_active}")
            y -= 20
        c.showPage()
        c.save()
        return response
    return render(request, 'reports/subscription_report.html', {'subscriptions': subscriptions})
