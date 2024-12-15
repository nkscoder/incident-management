from rest_framework import serializers
from .models import User , Incident

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'address', 'pin_code', 'city', 'country']

class IncidentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Incident
        fields = [
            'incident_id', 'user', 'reporter_name', 'details',
            'reported_at', 'priority', 'status'
        ]
        read_only_fields = ['incident_id', 'reported_at']

    def validate_status(self, value):
        if self.instance and self.instance.status == 'Closed':
            raise serializers.ValidationError("Closed incidents cannot be edited.")
        return value