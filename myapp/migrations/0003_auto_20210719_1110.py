# Generated by Django 2.2.24 on 2021-07-19 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210719_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='otherDepartement',
            field=models.CharField(blank=True, max_length=255, verbose_name='承接部门'),
        ),
        migrations.AlterField(
            model_name='info',
            name='taskDescription',
            field=models.CharField(blank=True, max_length=255, verbose_name='任务说明'),
        ),
    ]
