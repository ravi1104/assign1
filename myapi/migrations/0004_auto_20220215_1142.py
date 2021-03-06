# Generated by Django 3.2.3 on 2022-02-15 11:42

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_auto_20220215_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photodata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_first', models.CharField(max_length=80, verbose_name='First Name')),
                ('name_last', models.CharField(max_length=100, verbose_name='Last Name')),
                ('photo', versatileimagefield.fields.VersatileImageField(upload_to='photo/', verbose_name='photo')),
                ('photo_ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20)),
            ],
            options={
                'verbose_name': 'Photodata',
                'verbose_name_plural': 'Photodata',
            },
        ),
        migrations.DeleteModel(
            name='Alldata',
        ),
    ]
