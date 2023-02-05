from django.urls import path

from ticket.views import *

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('ticket/', TicketListView.as_view()),
    path('ticket/<int:pk>/', TicketDetailView.as_view()),
    path('ticket/update/<int:pk>/', TicketUpdateView.as_view()),
    path('message/', MessageCreateView.as_view()),
]
