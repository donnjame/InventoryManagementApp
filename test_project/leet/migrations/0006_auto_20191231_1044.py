# Generated by Django 3.0 on 2019-12-31 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leet', '0005_auto_20191231_1031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anthemasset',
            old_name='anthemuser',
            new_name='anthem_user',
        ),
    ]