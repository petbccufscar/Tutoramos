from django.db import models

# Create your models here.
class POT(models.Model):
    nome = models.CharField(blank=False, null=False, max_length=255)
    
    def __str__(self) -> str:
        return f"grupo {self.nome}"