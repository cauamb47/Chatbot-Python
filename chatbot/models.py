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


class Message(models.Model):
    """
    Representa uma mensagem enviada em uma conversa.
    """

    class Sender(models.TextChoices):
        USER = "USER", "Usuário"
        AI = "AI", "Inteligência Artificial"
        ATTENDANT = "ATTENDANT", "Atendente"

    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name="messages",
    )
    
    sender = models.CharField(
        max_length=20,
        choices=Sender.choices,
    )

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    tokens_used = models.IntegerField(default=0)

    response_time = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.sender} - {self.created_at:%d-%m-%y %H:%M}"
