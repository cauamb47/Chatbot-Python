from django.contrib import admin

from .models import Conversation, Message


class MessageInline(admin.TabularInline):
    model = Message
    extra = 0


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "usuario",
        "titulo",
        "status",
        "criada_em",
    )

    list_filter = (
        "status",
    )

    search_fields = (
        "usuario__username",
        "titulo",
    )

    inlines = [MessageInline]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "conversation",
        "sender",
        "created_at",
        "tokens_used",
    )

    list_filter = (
        "sender",
    )

    search_fields = (
        "content",
    )