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
        fields = ('id', 'email', 'password','Fname','DateOfBirth','phone_num','location','blood_group')
        extra_kwargs = {'password': {'write_only': True}, 'blood_group': {'required': False}}
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


