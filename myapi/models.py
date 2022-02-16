from django.db import models

from versatileimagefield.fields import VersatileImageField, PPOIField


class Alldata(models.Model):

    name = models.CharField('Name of fish', max_length=80)
    species = models.CharField(max_length=100)
    weight =models.DecimalField(
                         max_digits = 5,
                         decimal_places = 2)
    length = models.DecimalField(
                         max_digits = 5,
                         decimal_places = 2)
    latitude = models.DecimalField(
                         max_digits = 5,
                         decimal_places = 2)
    longitude = models.DecimalField(
                         max_digits = 5,
                         decimal_places = 2)
    timestamp =models.DateTimeField(auto_now_add=True)

    photo = VersatileImageField(
        'photo',
        upload_to='photo/',
        ppoi_field='photo_ppoi'
    )
    photo_ppoi = PPOIField()

    class Meta:
        verbose_name = 'Alldata'
        verbose_name_plural = 'Alldata'