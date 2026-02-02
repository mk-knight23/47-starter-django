"""
Serializers for User model and API endpoints.
"""
from rest_framework import serializers
from .models import User, UserProfile


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model."""

    full_name = serializers.SerializerMethodField()
    is_staff_user = serializers.BooleanField(read_only=True)
    is_admin_user = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'full_name',
            'phone',
            'avatar',
            'bio',
            'role',
            'is_staff',
            'is_superuser',
            'is_staff_user',
            'is_admin_user',
            'is_active',
            'email_verified',
            'date_joined',
            'updated_at',
            'last_seen',
            'language',
            'timezone',
        ]
        read_only_fields = [
            'id',
            'date_joined',
            'updated_at',
            'last_seen',
            'is_staff',
            'is_superuser',
        ]

    def get_full_name(self, obj):
        """Get user's full name."""
        return obj.get_full_name()


class UserCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating new users."""

    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password_confirm = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'password_confirm',
            'first_name',
            'last_name',
            'phone',
        ]

    def validate(self, attrs):
        """Validate passwords match."""
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({'password_confirm': 'Passwords do not match'})
        return attrs

    def create(self, validated_data):
        """Create user with encrypted password."""
        validated_data.pop('password_confirm')
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password, **validated_data)
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating user profile."""

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'phone',
            'avatar',
            'bio',
            'language',
            'timezone',
        ]


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for UserProfile model."""

    class Meta:
        model = UserProfile
        fields = [
            'address_line1',
            'address_line2',
            'city',
            'state',
            'postal_code',
            'country',
            'website',
            'linkedin',
            'github',
            'twitter',
            'notification_email',
            'notification_sms',
            'newsletter',
            'birth_date',
        ]
