from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'Electronics/home.html', {'products': products})

def about(request):
    return render(request, 'Electronics/about.html')

def contact(request):
    if request.method == 'POST':
        # Handle form submission here
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # You can add email sending logic here
        return render(request, 'Electronics/contact.html', {'success': True})
    return render(request, 'Electronics/contact.html')

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'Electronics/product_detail.html', {'product': product})

def cart(request):
    return render(request, 'Electronics/cart.html')

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'Electronics/add_product.html', {'form': form})






