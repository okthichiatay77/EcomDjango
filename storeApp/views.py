from django.shortcuts import render, redirect
from django.urls import reverse
from .models import SanPham, Shoe, Blog, Cart
from .forms import CartForm
# Create your views here.
def index(request):
    context = {}
    cl = SanPham.objects.all()

    context['clothes'] = cl

    if request.method == 'POST':
        item_id = request.POST['item_id']
        item_name = request.POST['item_name']
        item_image = request.POST['item_image']
        item_price = request.POST['item_price']
        item_quantity = request.POST['item_quantity']
        item_total = request.POST['item_total']

        cart = Cart.objects.create(item_id=item_id,item_name=item_name, item_image=item_image, item_price=item_price,
                                   item_quantity=item_quantity, item_total=item_total, user=request.user)
        cart.save()
        return redirect(reverse('store:index'))

    return render(request, 'index.html', context)

def list_woman(request):
    context = {}
    clothes_women = SanPham.objects.filter(kind_of_sp='women')
    context['clothes_women'] = clothes_women
    return render(request, 'store/list_woman.html', context)

def list_children(request):
    context = {}
    clothes_children = SanPham.objects.filter(kind_of_sp='children')
    context['clothes_children'] = clothes_children
    return render(request, 'store/list_children.html', context)

def list_shoes(request):
    context = {}
    list_shoe = Shoe.objects.all()
    context['shoes'] = list_shoe
    return render(request, 'store/list_shoes.html', context)

def list_filter_shoes(request, kind):
    context = {}
    list_shoe = Shoe.objects.filter(shoe_company=kind)
    context['filter_shoe'] = list_shoe
    return render(request, 'store/list_filter_shoes.html', context)

def product_detail(request, pk):
    sp = SanPham.objects.get(pk=pk)

    return render(request, 'store/product-details.html', {'sp':sp})

def shoe_detail(request, pk):
    shoes = Shoe.objects.get(pk=pk)

    return render(request, 'shoe_detail.html', {'shoe':shoes})

def blog(request):
    context = {}
    blogs = Blog.objects.all()
    context['blogs'] = blogs
    return render(request, 'blog.html', context)

def blog_single(request, pk):
    blog = Blog.objects.get(pk=pk)
    return render(request, 'blog-single.html', {'blog':blog})

def shop(request):
    return render(request, 'shop.html')

def detail(request):
    return render(request, 'details.html')

def check_out(request):
    return render(request, 'checkout.html')

def cart(request):
    carts = Cart.objects.filter(user=request.user)
    return render(request, 'store/cart.html', {'carts': carts})

def contact_us(request):
    return render(request, 'contact-us.html')

def error_404(request):
    return render(request, 'store/404.html')