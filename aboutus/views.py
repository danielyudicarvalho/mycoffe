from django.shortcuts import render, get_list_or_404, redirect
from .models import AboutUs
from .forms import AboutUsForm

def about_us_create(request):
    if request.method == 'POST':
        form = AboutUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aboutus:about_us_list')
    else:
        form = AboutUsForm()
    return render(request, 'aboutus/form.html', {
        'form': form,
        'title': 'Sobre Nós'
    })

def about_us(request):
    about_us_info = AboutUs.objects.first()  # Assuming you have only one About Us entry
    return render(request, 'about_us.html', {'about_us': about_us_info})

def about_us_edit(request,pk):
    about_us = get_list_or_404(AboutUs, pk=pk)
    if request.method == 'POST':
        form = AboutUsForm(request.POST, instance=about_us)
        if form.is_valid():
            form.save()
            return redirect('aboutus:about_us_list')
    else:
        form = AboutUsForm(instance=about_us)

    return render(request, 'aboutus/form.html', {'form':form})
# Create your views here.
