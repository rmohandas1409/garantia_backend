# Generated by Django 4.2.8 on 2023-12-26 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cliente", "0003_remove_cliente_ativo_remove_cliente_celular_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cliente",
            name="aceitarTermos",
            field=models.BooleanField(default="", max_length=3),
        ),
    ]
