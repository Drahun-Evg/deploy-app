from rest_framework import generics
from rest_framework.views import Response

from ticket.serializers import *

from .tasks import send_answer_email


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class TicketUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketUpdateSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            owner_queryset = self.queryset.all()
        return owner_queryset


class TicketDetailView(generics.RetrieveDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketDetailSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            owner_queryset = self.queryset.all()
        else:
            owner_queryset = self.queryset.filter(owner=self.request.user)
        return owner_queryset


class TicketListView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketListSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            queryset = Ticket.objects.all()
        else:
            queryset = Ticket.objects.filter(owner=request.user)
        serializer = TicketListSerializer(queryset, many=True)
        return Response(serializer.data)


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageListSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def post(self, request, *args, **kwargs):
        if request.user.is_staff:
            ticket_give = request.data.dict()
            id_ticket = ticket_give['ticket']
            text_1 = ticket_give['text']
            owner_email = Ticket.objects.get(id=id_ticket).owner.email
            owner_n = Ticket.objects.get(id=id_ticket).owner.username
            send_answer_email.delay(owner_email=owner_email, text_1=text_1, owner_n=owner_n)
        return self.create(request, *args, **kwargs)
