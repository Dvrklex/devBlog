from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Like

@receiver(post_save, sender=Like)
def like_post(sender, instance, created, **kwargs):
    if created:
        instance.post.likes += 1
        instance.post.save()
