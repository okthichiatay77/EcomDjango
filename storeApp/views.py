from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import *
from .forms import *
# Create your views here.
def index(request):
    context = {}
    cl = SanPham.objects.all()

    context['clothes'] = cl

    if request.method == 'POST':
        i_name = request.POST['item_name']
        i_id = request.POST['item_id']
        i_image = request.POST['item_image']
        i_price = request.POST['item_price']
        i_quantity = request.POST['item_quantity']
        i_name_object = request.POST['item_object']

        cart = CartEshop.objects.create(i_name=i_name, i_id=i_id, i_image=i_image, i_price=i_price,
                                        i_quantity=i_quantity, i_name_object=i_name_object,
                                        user=request.user)
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
    if request.method == 'POST':
        name = request.POST['shoe_name']
        price = request.POST['price']
        quantity = request.POST['quantity']
        id = request.POST['shoe_id']
        shoe_image = request.POST['shoe_image']

        add_to_cart = CartEshop.objects.create(i_name=name, i_image=shoe_image,
                                               i_quantity=quantity, i_price=price, i_id=id,
                                               user=request.user)
        add_to_cart.save()
        return redirect(reverse('/'))

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
    return render(request, 'store/shoe-details.html', {'shoe':shoes})

def blog(request):
    context = {}
    blogs = Blog.objects.all()
    context['blogs'] = blogs
    return render(request, 'blog.html', context)

def blog_single(request, pk):
    blog = Blog.objects.get(pk=pk)
    return render(request, 'blog-single.html', {'blog':blog})

@login_required
def cart(request):
    carts = CartEshop.objects.filter(user=request.user)

    if request.method == 'POST':
        id = int(request.POST['get_id'])
        obj = get_object_or_404(CartEshop, id=id)
        form = CartForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CartForm()


    return render(request, 'store/cart.html', {'carts':carts, 'form':form})

def shop(request):
    return render(request, 'shop.html')

def detail(request):
    return render(request, 'details.html')

def check_out(request):
    return render(request, 'checkout.html')

def contact_us(request):
    return render(request, 'contact-us.html')

def error_404(request):
    return render(request, 'store/404.html')