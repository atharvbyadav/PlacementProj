from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'Electronics/home.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'Electronics/product_detail.html', {'product': product})






