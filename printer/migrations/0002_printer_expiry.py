# Generated by Django 4.2.1 on 2023-07-12 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='printer',
            name='expiry',
            field=models.DateField(blank=True, null=True),
        ),
    ]
