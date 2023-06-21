import os
from binascii import hexlify

from django.db import models
from django_countries.fields import CountryField

from .validators import validate_range_level, validate_username_tag


# Create your models here.
class PlayerDemography(models.Model):
    """Model for the player demographics.

    This model is used to store the player information submitted by the user.
    """

    email = models.EmailField(max_length=254)
    """Email of the user/player."""
    name = models.CharField(max_length=100, null=True, blank=True)
    """Name of the user/player."""
    gender = models.CharField(max_length=10)
    """Gender of the player"""
    age = models.IntegerField()
    """Age of the player"""
    country = models.CharField(max_length=50)
    """Country of the player"""
    province = models.CharField(max_length=50)
    """Province of the player"""
    username = models.CharField(max_length=50, validators=[validate_username_tag])
    """Username tag of the player"""
    average_hours = models.IntegerField(verbose_name="How many hours do you play on average?")
    """Average hours that the player playing the game."""
    frequency = models.IntegerField(verbose_name="How often do you play?")
    """Frequency of the player playing a game."""
    in_game_rank = models.CharField(max_length=50, verbose_name="What is your in-game rank?")
    """In-game rank of the player."""
    in_game_rank_level = models.IntegerField(
        verbose_name="What is your in-game rank level?", validators=[validate_range_level], default=1
    )
    """In-game rank level of the player. it partners with the in_game_rank field."""
    often_server = models.CharField(max_length=50, verbose_name="In which server do you play the most?")
    """Server where the player plays the most."""

    @property
    def report_entries_count(self):
        return self.player_entries.count()  # type: ignore

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name_plural = "Player Demographics"


def content_file_name(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s_%s.%s" % (instance.id, instance.player_id.pk, ext)
    return os.path.join("chat_screenshots", filename)


class Entry(models.Model):
    """Model for the report entry.

    This model is used to store the report entry submitted by the user. like the screenshots and text.
    """

    def generate_id():
        """Generate a random id for the entry.

        Reference: https://zindilis.com/posts/hex-primary-key-in-django-model/
        """
        possible = hexlify(os.urandom(4)).decode()
        while True:
            try:
                Entry.objects.get(id=possible)
            except Entry.DoesNotExist:
                return possible

    id = models.CharField(max_length=8, primary_key=True, default=generate_id, editable=False)
    """ID of the entry. in hex format."""
    player_id = models.ForeignKey(to=PlayerDemography, on_delete=models.CASCADE, related_name="player_entries")
    """Player ID of who entry belongs to."""
    date_created = models.DateField(auto_now_add=True)
    """Date when the entry was created."""
    text = models.CharField(max_length=1000, null=True, blank=True)
    """Text of the entry. This is the chat message."""
    screenshot = models.ImageField(upload_to=content_file_name, null=True, blank=True)
    """Screenshot of the entry. This is the screenshot of the chat."""
    description = models.TextField(null=True, blank=True)
    """Description of the entry. This is the description of the entry."""
    emotion = models.CharField(max_length=50, null=True, blank=True)
    """Emotion Label of the entry."""
    toxicity = models.CharField(max_length=50, null=True, blank=True)
    """Toxicity Label of the entry."""
    sentiment = models.CharField(max_length=50, null=True, blank=True)
    """Sentiment Label of the entry."""

    class Meta:
        ordering = ["-date_created"]
        verbose_name_plural = "Entries"
