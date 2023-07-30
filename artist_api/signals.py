# artist_api/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Artist

@receiver(post_save, sender=User)
def create_artist(sender, instance, created, **kwargs):
    if created:
        Artist.objects.create(name=instance.username, user=instance)

@receiver(post_save, sender=User)
def save_artist(sender, instance, **kwargs):
    instance.artist.save()
