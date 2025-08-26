from django.db import models

class Expert(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, primary_key=True)
    prompt = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)

class Reflection(models.Model):
    participant = models.ForeignKey('pages.Participant', on_delete=models.CASCADE)
    reflectionType = models.ForeignKey('Expert', on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)