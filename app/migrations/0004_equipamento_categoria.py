# Generated by Django 4.2.7 on 2023-11-08 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipamento',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='equipamento', to='app.categoria'),
        ),
    ]