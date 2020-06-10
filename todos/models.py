from django.db import models
from django.utils import timezone

# Create your models here.


class Todo(models.Model):
    theme = models.CharField(max_length=200, unique=True)
    inscription = models.CharField(max_length=200, unique=True)
    ordered_at = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    cake_thumb = models.URLField()
    client = models.CharField(max_length=200, unique=True)
    flavors = models.TextField()

    class Meta:
        ordering = ('-delivery_date',)

    class Meta:
        verbose_name = 'todo'
        verbose_name_plural = 'todos'

    def __str__(self):
        return self.client
