# Generated by Django 2.0 on 2017-12-15 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_auto_20171215_1726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='detais',
            new_name='details',
        ),
    ]
