# Generated by Django 3.2.3 on 2022-02-15 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_auto_20220215_1120'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Alldata',
        ),
        migrations.AlterModelOptions(
            name='alldata',
            options={'verbose_name': 'Alldata', 'verbose_name_plural': 'Alldata'},
        ),
    ]
