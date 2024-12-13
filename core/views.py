from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated,BasePermission
from .models import User, Incident
from .serializers import UserSerializer, IncidentSerializer

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

# User Views
class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

# Incident Views
class IncidentListCreateAPIView(ListCreateAPIView):
    serializer_class = IncidentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Incident.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class IncidentRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = IncidentSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Incident.objects.filter(user=self.request.user)
