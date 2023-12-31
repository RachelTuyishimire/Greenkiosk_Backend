# Generated by Django 4.2.1 on 2023-06-19 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Available_products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price_per_quantity', models.DecimalField(decimal_places=2, max_digits=8)),
                ('available_quantity', models.PositiveIntegerField()),
                ('condition', models.CharField(max_length=255)),
                ('shipping_cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('taxes', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
