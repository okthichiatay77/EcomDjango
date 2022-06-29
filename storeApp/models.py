from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.
availabilityList = [
    ('còn hàng', 'Còn Hàng'),
    ('hết hàng', 'Hết Hàng'),
    ('dừng sản xuất', 'Dừng Sản Xuất'),
]

conditionList = [
    ('mới', 'Mới'),
    ('cũ', 'Cũ'),
    ('sale', 'Sale')
]

brandList = [
    ('chanel', 'CHANEL'),
    ('gucci', 'GUCCI'),
    ('dior', 'DIOR'),
    ('louis vuitton', 'LOUIS VUITTON'),
    ('dolce & cabbana', 'DOLCE & GABBANA'),
    ('hermes', 'HERMÈS'),
    ('versace', 'VERSACE'),
    ('prada', 'PRADA'),
    ('fendi', 'FENDI'),
    ('guess', 'GUESS'),
    ('valentino', 'VALENTINO'),
    ('armani', 'ARMANI'),
    ('vn', 'Hàng nội địa'),
]

type_product = [
    ('men', 'Nam'),
    ('women', 'Nữ'),
    ('children', 'Trẻ Em')
]

class SanPham(models.Model):
    sp_image = models.ImageField(_('image'), upload_to='sp_images')
    name = models.CharField(_('name'), max_length=100)
    price = models.IntegerField(_("price"))
    availability = models.CharField(_('availability'), choices=availabilityList, max_length=20)
    condition = models.CharField(_('condition'), choices=conditionList, max_length=20)
    brand = models.CharField(_('brand'), choices=brandList, max_length=20)
    kind_of_sp = models.CharField(_('product type'), choices=type_product, max_length=20)

    def __str__(self):
        return self.name

hang_san_xuat = [
    ('NIKE', 'NIKE'),
    ('UNDER ARMOUR', 'UNDER ARMOUR'),
    ('ADIDAS', 'ADIDAS'),
    ('PUMA', 'PUMA'),
    ('ASICS', 'ASICS'),
    ('vn', 'Hàng nội địa'),
    ('Biti\'s', 'Biti\'s'),
    ('Bita\'s', 'Bita\'s'),
    ('JUNO', 'JUNO'),
    ('ANANAS', 'ANANAS'),
    ('MỘT', 'MỘT'),
    ('Vina Giầy', 'Vina Giầy'),
    ('RieNevan', 'RieNevan'),
    ('Kim Thành', 'Kim Thành'),
    ('COX Shoes', 'COX Shoes'),
    ('Đông Hải', 'Đông Hải'),
]

kind_shoe_list = [
    ('giày thể thao', 'Giày Thể Thao'),
    ('giày tây', 'Giày Tây'),
    ('thường', 'Thường')
]

class Shoe(models.Model):
    shoe_image = models.ImageField(_('shoe image'), upload_to='shoe_images')
    shoe_name = models.CharField(_('shoe name'), max_length=200)
    shoe_company = models.CharField(_('shoe company'), choices=hang_san_xuat, max_length=50)
    price = models.IntegerField(_('price'))
    size = models.IntegerField(_('size of shoes'))
    availability = models.CharField(_('availability'), choices=availabilityList, max_length=20)
    condition = models.CharField(_('condition'), choices=conditionList, max_length=20)
    kind_shoe = models.CharField(choices=kind_shoe_list, max_length=20)
    kind_of_shoe = models.CharField(_('product type'), choices=type_product, max_length=20)

    def __str__(self):
        return self.shoe_name


brandBagList = [
    ('Coach', 'COACH'),
    ('Chanel', 'CHANEL'),
    ('JW Anderson', 'JW ANDERSON'),
    ('Celine', 'CELINE'),
    ('Christian Dior', 'CHRISTIAN DIOR'),
    ('Gucci', 'GUCCI'),
    ('Louis Vuitton', 'LOUIS VUITTON'),
    ('Prada', 'PRADA'),
    ('Valentino', 'VALENTINO'),
    ('Hermes', 'HERMES'),
    ('vn', 'Hàng nội địa'),
]

class Tui(models.Model):
    bag_image = models.ImageField(upload_to='bag_images')
    bag_name = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    number_of_compartment = models.IntegerField()
    availability = models.CharField(_('availability'), choices=availabilityList, max_length=20)
    condition = models.CharField(_('condition'), choices=conditionList, max_length=20)
    price = models.IntegerField()
    bag_brand = models.CharField(_('bag brand'), choices=brandBagList, max_length=50)
    kind_of_bag = models.CharField(_('type bag'), choices=type_product, max_length=20)

    def __str__(self):
        return self.bag_name



class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image_blog = models.ImageField(upload_to='blog_images')
    time_created = models.TimeField(auto_now=True)
    author = models.CharField(max_length=100)


    def __str__(self):
        return self.title



class Cart(models.Model):
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=200)
    item_image = models.ImageField(upload_to='cart_images')
    item_price = models.IntegerField()
    item_quantity = models.IntegerField()
    item_total = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_cart')

    def __str__(self):
        return self.item_name

