from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Asset, Maintenance

@receiver(post_save, sender=Asset)
def create_maintenance_for_asset(sender, instance, created, **kwargs):
    if created:
        Maintenance.objects.create(asset=instance, name=instance.name, date=instance.date)
