from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password','Fname','DateOfBirth','phone_num','location','blood_group')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
        validated_data['email'], 
        validated_data['password'],
        validated_data['Fname'],
        validated_data['DateOfBirth'],
        validated_data['phone_num'],
        validated_data['location'],
        validated_data['blood_group'],
        )
       
        user.save()
        Token.objects.create(user = user)


        return user


