from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Product

from django.http import HttpResponse
from . serializers import ProductCreate


def index(request):
    shelf = Product.objects.all()
    return render(request, 'library.html', {'shelf': shelf})

def upload(request):
    upload = ProductCreate()
    if request.method == 'POST':
        upload = ProductCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'Upload_form.html', {'upload_form':upload})

def update_Product(request, Product_id):
    Product_id = int(Product_id)
    try:
        Product_sel = Product.objects.get(id = Product_id)
    except Product.DoesNotExist:
        return redirect('index')
    Product_form = ProductCreate(request.POST or None, instance = Product_sel)
    if Product_form.is_valid():
       Product_form.save()
       return redirect('index')
    return render(request, 'Upload_form.html', {'upload_form':Product_form})

def delete_Product(request, Product_id):
    Product_id = int(Product_id)
    try:
        Product_sel = Product.objects.get(id = Product_id)
    except Product.DoesNotExist:
        return redirect('index')
    Product_sel.delete()
    return redirect('index')