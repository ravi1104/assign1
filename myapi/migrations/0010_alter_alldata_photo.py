# Generated by Django 3.2.3 on 2022-02-16 15:26

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0009_alter_alldata_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alldata',
            name='photo',
            field=versatileimagefield.fields.VersatileImageField(default='', null=True, upload_to='photo/', verbose_name='photo'),
        ),
    ]