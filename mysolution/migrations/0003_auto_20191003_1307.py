# Generated by Django 2.2 on 2019-10-03 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysolution', '0002_auto_20191003_1303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mysolution',
            old_name='grade',
            new_name='name',
        ),
    ]
