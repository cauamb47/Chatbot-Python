from django.conf import settings
from django.db import models


class Conversation(models.Model):
    """
    Representa uma conversa entre um usuário e o chatbot.
    """

    class Status(models.TextChoices):
        ABERTA = "ABERTA", "Aberta"
        FECHADA = "FECHADA", "Fechada"
        AGUARDANDO = "AGUARDANDO", "Aguardando atendente"

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="conversations",
    )

    titulo = models.CharField(
        max_length=150,
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ABERTA,
    )

    criada_em = models.DateTimeField(auto_now_add=True)

    atualizada_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.titulo or 'Nova conversa'}"