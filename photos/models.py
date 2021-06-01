from django.db import models
from datetime import datetime

# Create your models here.
class Photo(models.Model):
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.description

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)