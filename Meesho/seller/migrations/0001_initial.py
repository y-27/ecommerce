# Generated by Django 4.1.5 on 2023-05-15 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0005_alter_seller_phone_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('stock', models.IntegerField()),
                ('code', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='product/')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.seller')),
            ],
            options={
                'db_table': 'product_tb',
            },
        ),
    ]