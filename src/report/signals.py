from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Entry, PlayerDemography


@receiver(post_save, sender=Entry)
def create_report(sender, instance, created, **kwargs):
    if created and instance.screenshot is not None:
        instance.screenshot.name = f"{instance.id}.png"
        instance.save()
        from .tasks import process_image

        print(instance.screenshot.path)
        data = process_image(instance.screenshot.path)

        with transaction.atomic():
            try:
                for key, value in enumerate(data):
                    Entry.objects.create(player_id=instance.player_id, text=value)
                transaction.commit()
            except Exception as e:
                transaction.rollback()
