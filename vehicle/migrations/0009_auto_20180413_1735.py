# Generated by Django 2.0.4 on 2018-04-13 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0008_vehicle_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to='vehicle_image'),
        ),
    ]