from django.db import models
from Perfil.models import Perfil
from POT.models import POT

# Create your models here.
class Reuniao(models.Model):
    nome = models.CharField(blank=False, null=False, max_length=255)
    descricao = models.CharField(blank=False, null=False, max_length=400)
    data_hora = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    participantes = models.ManyToManyField(Perfil,
        related_name="reunioes_do_perfil") 
    POT = models.ForeignKey(POT, models.CASCADE, 
        related_name="reunioes_do_pot")
    
    def __str__(self) -> str:
        return f"{self.nome} {self.data_hora}"
