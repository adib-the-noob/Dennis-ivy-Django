from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name