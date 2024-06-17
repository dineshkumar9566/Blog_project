from .models import User,Token
from rest_framework import serializers
from rest_framework_simplejwt.settings import api_settings

# Serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'contact_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create a new user instance using the validated data
        user = User(
            username = validated_data['username'],
            email=validated_data['email'],
            contact_number = validated_data['contact_number'],
        )
        user.set_password(validated_data['password'])
        user.save()
        
        # Return the created user
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

# Serializer for the Token model
class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'