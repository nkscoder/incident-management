from django.urls import path
from .views import UserListCreateAPIView, UserRetrieveUpdateAPIView, IncidentListCreateAPIView, IncidentRetrieveUpdateAPIView, CustomAuthToken

urlpatterns = [
    path('api/users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('api/users/<int:pk>/', UserRetrieveUpdateAPIView.as_view(), name='user-retrieve-update'),
    path('api/incidents/', IncidentListCreateAPIView.as_view(), name='incident-list-create'),
    path('api/incidents/<int:pk>/', IncidentRetrieveUpdateAPIView.as_view(), name='incident-retrieve-update'),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
]
