from django.http import Http404, HttpResponse
from django.shortcuts import render
from home.models import san_pham

# Create your views here.
def index(request):
    response = HttpResponse()
    response.write("<h2>Hello World</h2>")
    return response

def showProduct(request):
    products = san_pham.objects.all()
    return render(request, 'index.html', {'products': products})

def ProductDetail(request, id):
    try:
        products = san_pham.objects.get(pk=id)
    except san_pham.DoesNotExist:
        raise Http404('san pham khong ton tai')
    return render(request, 'productDetail.html', {'products': products})