from rest_framework import serializers
from django.contrib.auth.models import User

class bookserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']

