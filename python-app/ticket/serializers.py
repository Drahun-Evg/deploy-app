from rest_framework import serializers

from ticket.models import *


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        exclude = ['owner']


class MessageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Message
        exclude = ['ticket', 'id']


class TicketUpdateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Ticket
        fields = '__all__'


class TicketListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ['status']


class TicketDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    messages = MessageSerializer(many=True)

    class Meta:
        model = Ticket
        fields = ('id', 'owner', 'title', 'description', 'status', 'created', 'messages')


class MessageListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Message
        fields = ('id', 'owner', 'ticket', 'text', 'created')

    def __init__(self, *args, **kwargs):
        super(MessageListSerializer, self).__init__(*args, **kwargs)
        user = self.context['request'].user
        if user.is_staff:
            self.fields['ticket'].queryset = Ticket.objects.filter(status='unsolved')
        else:
            self.fields['ticket'].queryset = Ticket.objects.filter(owner=user).filter(status='unsolved')


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class UserDetailSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'tickets')
