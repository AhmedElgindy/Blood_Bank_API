from rest_framework import serializers
from .models import BloodRequest


class BloodRequestSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    Fname = serializers.CharField(source='user.Fname', read_only=True)
    location = serializers.CharField(source='user.location', read_only=True)
 
    class Meta:
        model = BloodRequest
        fields = "__all__"

    