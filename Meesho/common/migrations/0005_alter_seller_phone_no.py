# Generated by Django 4.1.5 on 2023-05-15 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_alter_seller_address_alter_seller_company_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='phone_no',
            field=models.BigIntegerField(default=1),
        ),
    ]
