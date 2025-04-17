from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm

# Create your views here.
def home(request):
    products = Product.objects.all()
    fm = ProductForm()
    return render(request, 'Electronics/home.html', {'products': products, 'fm': fm})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'Electronics/product_detail.html', {'product': product})






