# Generated by Django 4.2.4 on 2023-08-29 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw_2_app', '0006_alter_product_add_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateField(auto_now_add=True),
        ),
    ]