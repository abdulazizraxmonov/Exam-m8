from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser  
from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        validated_data['email'] = validated_data['email']
        user = CustomUser.objects.create_user(**validated_data)  
        return user

    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'email', 'organization', 'login', 'password', 'Scienfig_degree', 'Another_information', 'photo']



class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError('Invalid username or password')

        refresh = RefreshToken.for_user(user)
        attrs['refresh'] = str(refresh)
        attrs['access'] = str(refresh.access_token)

        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()


class EmailConfirmationSerializer(serializers.Serializer):
    email = serializers.EmailField()


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'photo']