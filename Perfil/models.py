from django.db import models
from django.contrib.auth.models import User
from POT.models import POT

# Create your models here.
class Perfil(models.Model):
    cor_favorita = models.CharField(blank=False, null=False, max_length=255)
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, 
        related_name='perfil')
    POT = models.ForeignKey(POT, on_delete=models.CASCADE, 
        related_name="potianos")

    def __str__(self) -> str:
        return f"{self.user.get_full_name()} do {self.POT}"