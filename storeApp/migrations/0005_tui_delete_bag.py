# Generated by Django 4.0.5 on 2022-06-27 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeApp', '0004_noithat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tui',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bag_image', models.ImageField(upload_to='bag_images')),
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
        migrations.DeleteModel(
            name='Bag',
        ),
    ]
