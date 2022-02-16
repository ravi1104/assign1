# Generated by Django 3.2.3 on 2022-02-15 11:20

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_first', models.CharField(max_length=80, verbose_name='First Name')),
                ('name_last', models.CharField(max_length=100, verbose_name='Last Name')),
                ('headshot', versatileimagefield.fields.VersatileImageField(upload_to='headshots/', verbose_name='Headshot')),
                ('headshot_ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20)),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'People',
            },
        ),
        migrations.DeleteModel(
            name='Apidata',
        ),
    ]
