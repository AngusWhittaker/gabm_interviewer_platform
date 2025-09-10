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

class BulkQuestion(models.Model):
    participant = models.ForeignKey('pages.Participant', on_delete=models.CASCADE)
    brain = models.CharField(max_length=100, null=False, blank=False)
    filename = models.CharField(max_length=255, null=False, blank=False)
    reflectionType = models.CharField(max_length=100, null=True, blank=True)
    filepath = models.CharField(max_length=255, null=False, blank=False)
    totalQuestions = models.IntegerField(null=False, blank=False, default=0)
    processedQuestions = models.IntegerField(null=False, blank=False, default=0)
    created = models.DateTimeField(auto_now_add=True)