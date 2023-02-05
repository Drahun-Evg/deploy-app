from django.contrib import admin

from .models import *


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'owner', 'created')
    list_filter = ('status',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('text', 'ticket', 'owner', 'created')
