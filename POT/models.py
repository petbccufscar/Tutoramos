from django.db import models

# Create your models here.
class POT(models.Model):
    nome = models.CharField(blank=False, null=False, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
