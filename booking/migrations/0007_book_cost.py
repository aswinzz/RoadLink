# Generated by Django 2.0.4 on 2018-04-12 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_book_distance'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cost',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=20),
        ),
    ]