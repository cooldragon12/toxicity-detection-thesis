from django.db import models
from binascii import hexlify
from django_countries.fields import CountryField
import os

from .validators import validate_username_tag
# Create your models here.
class PlayerDemography(models.Model):
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=50,null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    country =CountryField()
    province = models.CharField(max_length=50)
    ethnicity = models.CharField(max_length=50)
    username = models.CharField(max_length=50, validators=[validate_username_tag])
    average_hours = models.IntegerField(verbose_name='How many hours do you play on average?')
    frequency = models.IntegerField(verbose_name='How often do you play?')
    in_game_rank = models.CharField(max_length=50, verbose_name='What is your in-game rank?')
    often_server = models.CharField(max_length=50, verbose_name='In which server do you play the most?')
    def __str__(self) -> str:
        return self.username
    class Meta:
        verbose_name_plural = 'Player Demographics'
class Entry(models.Model):
    def generate_id():
        """Generate a random id for the entry.
        
        Reference: https://zindilis.com/posts/hex-primary-key-in-django-model/
        """
        possible = hexlify(os.urandom(4))
        while True:
            try:
                Entry.objects.get(id=possible)
            except Entry.DoesNotExist:
                return possible
    id = models.CharField(max_length=8, primary_key=True, default=generate_id, editable=False)
    player_id = models.ForeignKey(to=PlayerDemography, on_delete=models.CASCADE, related_name='player_entries')
    date_created = models.DateField(auto_now_add=True)
    text = models.CharField(max_length=1000)
    screenshot = models.ImageField(upload_to='chat_screenshots', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    emotion = models.CharField(max_length=50, null=True, blank=True)
    toxicity = models.CharField(max_length=50, null=True, blank=True)
    sentiment = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name_plural = 'Entries'
