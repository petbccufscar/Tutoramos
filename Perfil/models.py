from django.db import models
from django.contrib.auth.models import User
from POT.models import POT
# Create your models here.
class Perfil(models.Model):
    # Campos
    cor = models.CharField(blank=False, null=False, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    # Relações
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    POT = models.ForeignKey(POT, on_delete=models.CASCADE, related_name="participantes")
   