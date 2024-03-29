# Generated by Django 4.2.8 on 2023-12-24 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
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
                ("nome", models.CharField(default="", max_length=150)),
                ("nascimento", models.DateField(max_length=20)),
                ("cpf", models.CharField(default="", max_length=20, unique=True)),
                ("cidade", models.CharField(default="", max_length=100)),
                ("genero", models.CharField(default="", max_length=2)),
                ("estado", models.CharField(default="", max_length=100)),
                ("telefone", models.CharField(default="", max_length=14)),
                ("email", models.EmailField(default="", max_length=150, unique=True)),
                ("confirmarEmail", models.CharField(default="", max_length=150)),
                ("senha", models.CharField(default="", max_length=150)),
                ("confirmarSenha", models.CharField(default="", max_length=150)),
                ("aceitarTermos", models.CharField(default="", max_length=150)),
                ("rg", models.CharField(default="", max_length=9)),
                ("celular", models.CharField(default="", max_length=11)),
                ("ativo", models.BooleanField(default=True)),
            ],
        ),
    ]
