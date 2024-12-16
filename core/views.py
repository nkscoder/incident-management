from rest_framework.generics import  RetrieveUpdateAPIView,CreateAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated,BasePermission,AllowAny
from .models import  Incident
from .serializers import UserSerializer, IncidentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.filters import SearchFilter
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication




class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        print("IsOwner",obj.user)
        return obj.user == request.user

# User Views
class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            # Hash the password and save the user
            user = serializer.save(password=make_password(data.get('password')))
            # Create a token for the new user
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "User registered successfully!",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        
class CustomAuthToken(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = TokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Validate user credentials
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)

        # Generate JWT tokens
        refresh = serializer.validated_data['refresh']
        access = serializer.validated_data['access']

        return Response({
            "message": "User logged in successfully!",
            "refresh": refresh,
            "access": access,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            }
        }, status=status.HTTP_200_OK)        


class CreateIncidentAPIView(CreateAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        print( "Creating Incident from", self.request.user  )
        serializer.save(user=self.request.user)
            
            
# Incident Views
class ListIncidentAPIView(ListAPIView):
    serializer_class = IncidentSerializer
    authentication_classes = [JWTAuthentication]
    filter_backends = [SearchFilter]
    search_fields = ['incident_id', 'reporter_name', 'priority', 'status']

    def get_queryset(self):

        
        if not self.request.user.is_authenticated:
            print("User is not authenticated.")
        
        queryset = Incident.objects.all()
        user_filter = self.request.query_params.get('user_filter', 'true').lower()
        if user_filter == 'true':
            queryset = queryset.filter(user=self.request.user)
        return queryset

class IncidentRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = IncidentSerializer
    permission_classes = [JWTAuthentication, IsOwner]

    def get_queryset(self):
        return Incident.objects.filter(user=self.request.user)
