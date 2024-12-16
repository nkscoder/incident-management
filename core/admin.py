from django.contrib import admin
from .models import User, Incident

# User Admin
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'phone_number', 'city', 'country')
    search_fields = ('username', 'email', 'phone_number', 'city', 'country')
    list_filter = ('city', 'country')
    ordering = ('id',)

# Incident Admin
@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('incident_id', 'user', 'reporter_name', 'priority', 'status', 'reported_at')
    search_fields = ('incident_id', 'reporter_name', 'details', 'user__username')
    list_filter = ('priority', 'status', 'reported_at')
    ordering = ('-reported_at',)
    readonly_fields = ('incident_id', 'reported_at')
