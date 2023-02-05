from django.contrib.auth.models import User
from django.db import models


class Ticket(models.Model):
    STATUS_CHOICES = [
        ('unsolved', 'Нерешенный'),
        ('solved', 'Решенный'),
        ('frozen', 'Заморожен')
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='unsolved')
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='tickets')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Message(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='messages')
    text = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
