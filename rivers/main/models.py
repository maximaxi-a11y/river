from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
import datetime




class Item(models.Model):
    Item_name = models.CharField(max_length=200)
    Item_descr = models.TextField()
    pub_date = models.DateTimeField("date published",default=datetime.date.today)
    it_image = models.ImageField(upload_to='items', blank=True, null=True)
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.Item_name

class ItemImage(models.Model):
    product = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='items/')
    alt_text = models.CharField(max_length=255, blank=True, null=True)

@receiver(post_delete, sender=Item)
def delete_image_on_ad_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
    def __str__(self):
            return self.Item_name