from datetime import datetime, timedelta

from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Cliente(models.Model):
    cnpj = models.CharField(
        unique=True,
        max_length=14,
        null=False,
        blank=False
    )
    razao_social = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    nome_fantasia = models.CharField(
        max_length=100,
        null=True,
    )

    telefone = models.CharField(
        max_length=11,
        null=True,
        blank=False,
    )
    logradouro = models.CharField(
        max_length=100,
        null=True,
    )
    cidade = models.CharField(
        max_length=100,
    )

    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Clientes"
    def __str__(self):
        return self.razao_social

    def get_absolute_url(self):
        return reverse('cliente_detail', args=[str(self.id)])
    
class Categoria(models.Model):
    nome = models.CharField(
        unique=True,
        max_length=50,
        null=False,
        blank=False,
    )
    
    def __str__(self):
        """String for representing the Model object."""
        return self.nome

class Equipamento(models.Model):
    cliente = models.ForeignKey('Cliente', related_name='equipamento', on_delete=models.CASCADE, null=True)
    nome = models.CharField(
        unique=True,
        max_length=50,
        null=False,
        blank=False,
    )
    
    categoria = models.ForeignKey('Categoria', related_name='equipamento', on_delete=models.SET_NULL, null=True)

    is_active = models.BooleanField(default=True, null=False)

    assembled_on = models.DateTimeField(default=datetime.now, blank=True)

    cod_serie = models.CharField(
        max_length=14,
        default='00000000000000',
        null=False,
        blank=False
    )

    class Meta:
      verbose_name_plural = "Equipamentos"

    def __str__(self):
        """String for representing the Model object."""
        return self.nome
    
    def get_absolute_url(self):
        return reverse('equipamento_detail', args=[str(self.pk)])
