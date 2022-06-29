from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('list-women/', views.list_woman, name='list_woman'),
    path('list-children/', views.list_children, name='list_children'),
    path('list-shoes/', views.list_shoes, name='list_shoes'),
    path('list-filter-shoes/<str:kind>/', views.list_filter_shoes, name='list_filter_shoes'),
    path('blog/', views.blog, name='blog'),
    path('shop/', views.shop, name='shop'),
    path('product-detail/<int:pk>/', views.product_detail, name='product_detail'),
    path('shoe-detail/<int:pk>/', views.shoe_detail, name='shoe_detail'),
    path('check-out/', views.check_out, name='check_out'),
    path('details/', views.detail, name='detail'),
    path('cart/', views.cart, name='cart'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('error-404/', views.error_404, name='error'),
    path('blog-single/<int:pk>/', views.blog_single, name='blog_single'),
]