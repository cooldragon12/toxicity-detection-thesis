from django.db import models
from django.contrib.auth.models import AbstractUser, AnonymousUser

# Create your models here.
class User(AbstractUser):
    """User could access the system."""
    pass

class AnonymousParticipants(AnonymousUser):
    """Anonymous user could access the system."""
    pass