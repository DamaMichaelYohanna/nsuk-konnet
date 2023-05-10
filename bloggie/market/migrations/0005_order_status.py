# Generated by Django 4.1.7 on 2023-03-22 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_order_storeorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('processing', 'processing'), ('Done', 'Done')], default='pending', max_length=12),
        ),
    ]