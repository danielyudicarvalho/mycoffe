from django.shortcuts import render
from .models import AboutPage

def about_page(request):
    page_info = AboutPage.objects.first()
    return render(request, 'about_us/about_page.html', {'page_info': page_info})
