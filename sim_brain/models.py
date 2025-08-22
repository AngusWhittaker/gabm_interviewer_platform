from django.db import models

class Expert(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    prompt = models.TextField(null=False, blank=False)