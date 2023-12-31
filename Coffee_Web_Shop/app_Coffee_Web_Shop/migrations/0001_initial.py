# Generated by Django 4.2.7 on 2023-11-28 09:19

import datetime
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
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(default=datetime.datetime(2023, 11, 28, 10, 19, 27, 111399))),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('nr_available', models.IntegerField(default=0)),
                ('img', models.ImageField(upload_to='')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('description', models.CharField(blank=True, default='', max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Order_Detail',
            fields=[
                ('o_details_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_Coffee_Web_Shop.order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_Coffee_Web_Shop.product')),
            ],
        ),
    ]
