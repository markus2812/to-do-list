from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    dead_line = models.DateTimeField(
        null=True, blank=True, help_text="Enter the deadline date as you wish!"
    )
    is_completed = models.BooleanField(default=False, editable=True)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self):
        return self.title
