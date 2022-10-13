# Generated by Django 4.1.2 on 2022-10-13 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipt',
            name='total',
        ),
        migrations.AlterField(
            model_name='discount',
            name='discount',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.RemoveField(
            model_name='recipt',
            name='items',
        ),
        migrations.AddField(
            model_name='recipt',
            name='items',
            field=models.ManyToManyField(to='checkout.item'),
        ),
    ]
