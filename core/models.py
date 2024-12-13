from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
import random

# User Model
class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    pin_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.username

# Incident Model
class Incident(models.Model):
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    ]

    incident_id = models.CharField(max_length=15, unique=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incidents')
    reporter_name = models.CharField(max_length=100)
    details = models.TextField()
    reported_at = models.DateTimeField(default=now)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Open')

    def save(self, *args, **kwargs):
        if not self.incident_id:
            self.incident_id = f"RMG{random.randint(10000, 99999)}{now().year}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.incident_id
