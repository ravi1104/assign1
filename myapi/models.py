from django.db import models
from django.dispatch import receiver
from versatileimagefield.fields import VersatileImageField, PPOIField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer

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
        ppoi_field='photo_ppoi',null=True,default=""
    )
    photo_ppoi = PPOIField()

    class Meta:
        verbose_name = 'Alldata'
        verbose_name_plural = 'Alldata'

@receiver(models.signals.post_save, sender=Alldata)
def warm_Alldata_headshot_images(sender, instance, **kwargs):

    Alldata_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='photodata',
        image_attr='photo'
    )
    num_created, failed_to_create = Alldata_img_warmer.warm()