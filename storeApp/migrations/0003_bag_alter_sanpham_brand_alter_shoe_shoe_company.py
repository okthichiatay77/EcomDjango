# Generated by Django 4.0.5 on 2022-06-27 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeApp', '0002_shoe_alter_sanpham_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bag_name', models.CharField(max_length=100)),
                ('material', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('number_of_compartment', models.IntegerField()),
                ('availability', models.CharField(choices=[('còn hàng', 'Còn Hàng'), ('hết hàng', 'Hết Hàng'), ('dừng sản xuất', 'Dừng Sản Xuất')], max_length=20, verbose_name='availability')),
                ('condition', models.CharField(choices=[('mới', 'Mới'), ('cũ', 'Cũ'), ('sale', 'Sale')], max_length=20, verbose_name='condition')),
                ('price', models.IntegerField()),
                ('bag_brand', models.CharField(choices=[('Coach', 'COACH'), ('Chanel', 'CHANEL'), ('JW Anderson', 'JW ANDERSON'), ('Celine', 'CELINE'), ('Christian Dior', 'CHRISTIAN DIOR'), ('Gucci', 'GUCCI'), ('Louis Vuitton', 'LOUIS VUITTON'), ('Prada', 'PRADA'), ('Valentino', 'VALENTINO'), ('Hermes', 'HERMES'), ('vn', 'Hàng nội địa')], max_length=50, verbose_name='bag brand')),
                ('kind_of_bag', models.CharField(choices=[('men', 'Nam'), ('women', 'Nữ'), ('children', 'Trẻ Em')], max_length=20, verbose_name='type bag')),
            ],
        ),
        migrations.AlterField(
            model_name='sanpham',
            name='brand',
            field=models.CharField(choices=[('chanel', 'CHANEL'), ('gucci', 'GUCCI'), ('dior', 'DIOR'), ('louis vuitton', 'LOUIS VUITTON'), ('dolce & cabbana', 'DOLCE & GABBANA'), ('hermes', 'HERMÈS'), ('versace', 'VERSACE'), ('prada', 'PRADA'), ('fendi', 'FENDI'), ('guess', 'GUESS'), ('valentino', 'VALENTINO'), ('armani', 'ARMANI'), ('vn', 'Hàng nội địa')], max_length=20, verbose_name='brand'),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='shoe_company',
            field=models.CharField(choices=[('NIKE', 'NIKE'), ('UNDER ARMOUR', 'UNDER ARMOUR'), ('ADIDAS', 'ADIDAS'), ('PUMA', 'PUMA'), ('ASICS', 'ASICS'), ('vn', 'Hàng nội địa'), ("Biti's", "Biti's"), ("Bita's", "Bita's"), ('JUNO', 'JUNO'), ('ANANAS', 'ANANAS'), ('MỘT', 'MỘT'), ('Vina Giầy', 'Vina Giầy'), ('RieNevan', 'RieNevan'), ('Kim Thành', 'Kim Thành'), ('COX Shoes', 'COX Shoes'), ('Đông Hải', 'Đông Hải')], max_length=50, verbose_name='shoe company'),
        ),
    ]