# Generated by Django 4.1.2 on 2022-10-15 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Like",
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
                ("create_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ("-create_at",),
            },
        ),
    ]
