# Generated by Django 4.2.8 on 2023-12-21 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="fornecedor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("razao_social", models.CharField(max_length=100)),
                ("cpf_cnpj", models.CharField(max_length=15)),
                ("inscricao", models.CharField(max_length=15)),
                ("telefone", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=100)),
                ("endereco", models.CharField(max_length=100)),
                ("complemento", models.CharField(max_length=100)),
                ("bairro", models.CharField(max_length=100)),
                ("cidade", models.CharField(max_length=100)),
                ("estado", models.CharField(max_length=5)),
                ("cep", models.CharField(max_length=100)),
            ],
        ),
    ]
