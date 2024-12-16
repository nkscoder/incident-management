from django.urls import path
from .views import RegisterUserView, ListIncidentAPIView, CreateIncidentAPIView,IncidentRetrieveUpdateAPIView,CustomAuthToken


urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('incidents/create/', CreateIncidentAPIView.as_view(), name='create-incident'),
    path('incidents/list/', ListIncidentAPIView.as_view(), name='list-incident'),

    path('incidents/<int:pk>/', IncidentRetrieveUpdateAPIView.as_view(), name='incident-retrieve-update'),
    path('user/login/', CustomAuthToken.as_view(), name='api_token_auth'),
]
