# Generated by Django 3.2 on 2021-04-24 20:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Transfer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Transfer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='Transfer',
            name='tr_hash',
            field=models.UUIDField(default=uuid.UUID('cd72678c-ba89-4fec-b4f1-1c8bf5cec6b6')),
        ),
    ]
