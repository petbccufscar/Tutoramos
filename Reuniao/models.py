from django.db import models
from Perfil.models import Perfil
from POT.models import POT

# Create your models here.
class Reuniao(models.Model):
    # Campos
    nome = models.CharField(blank=False, null=False, max_length=255)
    descricao = models.CharField(blank=False, null=False, max_length=400)
    dataHora = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Relações
    participantes = models.ManyToManyField(Perfil,related_name="reunioes_do_perfil") 
    POT = models.ForeignKey(POT, models.CASCADE, related_name="reunioes_do_pot")