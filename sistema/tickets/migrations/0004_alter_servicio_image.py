# Generated by Django 5.0.6 on 2024-05-08 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_alter_servicio_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='image',
            field=models.ImageField(upload_to='tickets/images'),
        ),
    ]
