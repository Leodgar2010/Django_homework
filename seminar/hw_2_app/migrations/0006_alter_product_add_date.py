# Generated by Django 4.2.4 on 2023-08-29 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw_2_app', '0005_rename_name_product_title_alter_client_reg_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='add_date',
            field=models.DateField(),
        ),
    ]