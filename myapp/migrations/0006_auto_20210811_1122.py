# Generated by Django 2.2.24 on 2021-08-11 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_info_remark'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formname',
            old_name='days',
            new_name='workdays',
        ),
    ]
