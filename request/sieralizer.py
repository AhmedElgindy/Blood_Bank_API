from rest_framework import serializers
from .models import BloodRequest
from datetime import datetime
class BloodRequestSerializer(serializers.ModelSerializer):
    Fname = serializers.CharField(source='user.Fname', read_only=True)
    location = serializers.CharField(source='user.location', read_only=True)
 
    class Meta:
        model = BloodRequest
        fields = ['Fname','location','date','time']
   