# Generated by Django 3.2 on 2021-06-10 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20210610_1219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='image',
            new_name='logo',
        ),
    ]
