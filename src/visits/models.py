from django.db import models

# Create your models here.
class PageVisit(models.Model):
    path = models.TextField( blank=True, null=True)
    timstamp = models.DateTimeField(auto_now_add=True)
