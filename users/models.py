from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class UserType(models.TextChoices):
        CLIENTE = "CLIENTE", "Cliente"
        ATENDENTE = "ATENDENTE", "Atendente"
        ADMIN = "ADMIN", "Administrador"

    tipo = models.CharField(
        max_length=20,
        choices=UserType.choices,
        default=UserType.CLIENTE,
    )

    telefone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username