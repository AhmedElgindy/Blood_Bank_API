from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    Fname = serializers.CharField(max_length=50, required=True)
    DateOfBirth = serializers.DateField(required=True)
    password = serializers.CharField(max_length=100, write_only=True)
    email = serializers.EmailField(max_length=45,  required=True)
    phone_num = serializers.CharField(max_length=45,  required=True)
    location = serializers.CharField(max_length=45, required=True)
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password', 'Fname', 'DateOfBirth', 'phone_num', 'location', 'blood_group')
        extra_kwargs = {'password': {'write_only': True}, 'blood_group': {'required': False}}

    def validate_phone_num(self, value):
    # Add your phone number validation logic here
    # Example: Ensure the phone number is a number
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must be a number.")
        return value


    def validate_location(self, value):
    # Add your location validation logic here
    # Example: Ensure the location is not a string
        if isinstance(value, str):
            raise serializers.ValidationError("Location must not be a string.")
        return value


    def validate_Fname(self, value):
        # Add your Fname validation logic here
        # Example: Ensure the Fname contains only alphabetic characters
        if not value.isalpha():
            raise serializers.ValidationError("Fname should contain only alphabetic characters.")
        return value
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
        validated_data['email'], 
        validated_data['password'],
        validated_data['Fname'],
        validated_data['DateOfBirth'],
        validated_data['phone_num'],
        validated_data['location'],
        validated_data.get('blood_group'),
        )
       
        user.save()
        Token.objects.create(user = user)


        return user


