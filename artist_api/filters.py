# artist_api/models.py

from django.db import models
from django.contrib.auth.models import User

class Work(models.Model):
    WORK_TYPES = (
        ('YT', 'Youtube'),
        ('IG', 'Instagram'),
        ('OT', 'Other'),
    )

    link = models.URLField()
    work_type = models.CharField(max_length=2, choices=WORK_TYPES)

    def __str__(self):
        return self.link

class Artist(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    works = models.ManyToManyField(Work)

    def __str__(self):
        return self.name
