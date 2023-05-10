from rest_framework import serializers
from .models import BloodRequest,Donate


class BloodRequestSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    Fname = serializers.CharField(source='user.Fname', read_only=True)
    location = serializers.CharField(source='user.location', read_only=True)
    approved = serializers.BooleanField(read_only=True)
    blood_group =serializers.CharField(read_only = True)
    class Meta:
        model = BloodRequest
        fields = ['user','Fname','location','approved','blood_group']

class BloodRequestCreateSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    approved = serializers.BooleanField(read_only=True)
    blood_group =serializers.CharField(read_only = True)
    class Meta:
        model =BloodRequest
        fields = ['user','Fname','location','approved','blood_group']

class DonateSieralizer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    Fname = serializers.CharField(source='user.Fname', read_only=True)
    location = serializers.CharField(source='user.location', read_only=True)
    approved = serializers.BooleanField(read_only=True)
    blood_group =serializers.CharField(read_only = True)
    class Meta:
        model = Donate
        fields = '__all__'

class DonateSerializerCreate(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    approved = serializers.BooleanField(read_only=True)
    blood_group =serializers.CharField(read_only = True)
    class Meta:
        model =Donate
        fields = '__all__'

