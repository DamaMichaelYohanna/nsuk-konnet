# Generated by Django 4.1.7 on 2023-03-18 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_remove_product_contact_remove_product_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
