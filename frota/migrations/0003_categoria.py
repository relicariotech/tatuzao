# Generated by Django 4.2.7 on 2023-11-08 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frota', '0002_equipamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]