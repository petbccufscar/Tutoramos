from django.db import models

# Create your models here.
class Reuniao(models.Model):
    nome = models.CharField(blank=False, null=False, max_length=255)
    descricao = models.CharField(blank=False, null=False, max_length=400)
    dataHora = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)