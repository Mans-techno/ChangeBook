from rest_framework import serializers
from django.contrib.auth.models import User
from django.db.models import Avg
from .models import Profile


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Этот email уже занят')
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Пароли не совпадают')
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['username', 'email', 'city', 'phone', 'rating']

    def get_rating(self, obj):
        return obj.user.reviews.aggregate(Avg('rating'))['rating__avg']
