from django.shortcuts import render
from main.models import Banner,  Product, Category, Contact


def index(request):
    banners = Banner.objects.all()
    products = Product.objects.all()
    contact = Contact.objects.all()
    category = Category.objects.all()
    
    
    context = {
        'banners': banners,
        'product': products,
        'contact': contact,
        'category': category,
    }
    
    
    return render(request, 'front/index.html', context)





