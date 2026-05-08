# models.py
from django.db import models
from .utils import get_tmdb_profile

class Actress(models.Model):
    name = models.CharField(max_length=200,unique=True)
    profile_path = models.CharField(max_length=300, blank=True, null=True)

    def save(self, *args, **kwargs):

        if not self.profile_path:
            profile = get_tmdb_profile(self.name)
            if profile:
                self.profile_path = profile

        super().save(*args, **kwargs)