from django.shortcuts import render, get_object_or_404, redirect
from main.models import Banner
from .forms import BannerForm

def banner_list(request):
    banners = Banner.objects.all()
    return render(request, 'banner_list.html', {'banners': banners})

def banner_detail(request, pk):
    banner = get_object_or_404(Banner, pk=pk)
    return render(request, 'banner_detail.html', {'banner': banner})

def banner_create(request):
    if request.method == "POST":
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            banner = form.save()
            return redirect('banner_detail', pk=banner.pk)
    else:
        form = BannerForm()
    return render(request, 'banner_form.html', {'form': form})

def banner_update(request, pk):
    banner = get_object_or_404(Banner, pk=pk)
    if request.method == "POST":
        form = BannerForm(request.POST, request.FILES, instance=banner)
        if form.is_valid():
            banner = form.save()
            return redirect('banner_detail', pk=banner.pk)
    else:
        form = BannerForm(instance=banner)
    return render(request, 'banner_form.html', {'form': form})

def banner_delete(request, pk):
    banner = get_object_or_404(Banner, pk=pk)
    if request.method == "POST":
        banner.delete()
        return redirect('banner_list')
    return render(request, 'banner_confirm_delete.html', {'banner': banner})
