# Generated by Django 3.0 on 2020-01-11 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leet', '0011_anthemuser_internal_ext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anthemuser',
            name='internal_ext',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]