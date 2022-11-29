from django.db import models
from django.db.models import Count


class Blog(models.Model):
   title = models.CharField(max_length=200)
   description = models.TextField()
   date = models.DateField()

   def __str__(self):
      return self.title


