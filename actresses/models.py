from django.db import models
from .utils import get_tmdb_profile

class Actress(models.Model):
    name = models.CharField(max_length=200, unique=True)
    profile_path = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.profile_path:
            image_url = get_tmdb_profile(self.name)
            if image_url:
                self.profile_path = image_url
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name