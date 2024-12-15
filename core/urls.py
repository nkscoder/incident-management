from django.urls import path
from .views import UserListCreateAPIView, UserRetrieveUpdateAPIView, IncidentListCreateAPIView, IncidentRetrieveUpdateAPIView

urlpatterns = [
    path('user/login/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateAPIView.as_view(), name='user-retrieve-update'),
    path('incidents/', IncidentListCreateAPIView.as_view(), name='incident-list-create'),
    path('incidents/<int:pk>/', IncidentRetrieveUpdateAPIView.as_view(), name='incident-retrieve-update'),
]
