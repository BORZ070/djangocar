# Generated by Django 4.2.3 on 2023-09-11 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_bill'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='comment',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
