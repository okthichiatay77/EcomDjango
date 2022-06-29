from django.urls import path
from . import views

app_name = 'noithat'

urlpatterns = [
    path('', views.index_view, name='home_noithat'),
    path('blog/', views.blog_view, name='blog_noithat'),
    path('contact/', views.contact_view, name='contact_noithat'),
    path('product/', views.product_view, name='product_noithat'),
    path('product-detail/', views.product_detail_view, name='detail_noithat'),
    path('about', views.about_view, name='about_noithat'),
]