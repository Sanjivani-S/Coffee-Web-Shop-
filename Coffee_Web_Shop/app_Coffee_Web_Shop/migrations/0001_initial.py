# Generated by Django 4.2.7 on 2023-11-22 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_Coffee_Web_Shop.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('nr_available', models.IntegerField()),
                ('img', models.ImageField(upload_to='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Order_Detail',
            fields=[
                ('o_details_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_Coffee_Web_Shop.order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_Coffee_Web_Shop.product')),
            ],
        ),
    ]
