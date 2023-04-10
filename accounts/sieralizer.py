from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email','Fname','Lname','DateOfBirth','state','city','street','sex','phone_num','salary')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password','Fname','Lname','DateOfBirth','state','city','street','sex','phone_num','salary')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
        validated_data['email'], 
        validated_data['password'],
        validated_data['Fname'],
        validated_data['Lname'],
        validated_data['DateOfBirth'],
        validated_data['state'],
        validated_data['city'],
        validated_data['street'],
        validated_data['sex'],
        validated_data['phone_num'],
        validated_data['salary'],
        )
        user.save()
        Token.objects.create(user = user)


        return user


