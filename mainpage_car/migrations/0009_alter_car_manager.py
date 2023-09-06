# Generated by Django 4.2.3 on 2023-09-04 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_manager_info'),
        ('mainpage_car', '0008_car_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='about.manager'),
        ),
    ]