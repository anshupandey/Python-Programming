from django.shortcuts import render
from helloworld.models import products
# Create your views here.

def product_index(request):
    prod = products.objects.all()
    context = {'prod':prod}
    return render(request,'index.html',context)


def product_detail(request,pk):
    prod = products.objects.get(pk=pk)
    context = {"prod":prod}
    return render(request,"prod_detail.html",context)

