# Generated by Django 3.2.3 on 2022-02-16 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0008_alter_alldata_species'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alldata',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Name of fish'),
        ),
    ]
