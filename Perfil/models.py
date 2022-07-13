from django.db import models

# Create your models here.
class Perfil(models.Model):
    cor = models.CharField(blank=False, null=False, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)