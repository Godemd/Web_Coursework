# Generated by Django 5.1.3 on 2024-11-12 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("subject", models.CharField(blank=True, max_length=255, verbose_name="Тема сообщения")),
                ("body", models.TextField(verbose_name="Текст сообщения")),
            ],
            options={
                "verbose_name": "Сообщение",
                "verbose_name_plural": "Сообщения",
                "ordering": ["id"],
                "permissions": [("view_all_messages", "Can view all messages")],
            },
        ),
    ]
