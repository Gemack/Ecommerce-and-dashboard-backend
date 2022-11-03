from rest_framework.validators import ValidationError
from rest_framework import serializers
from .models import User


class RegisterUser(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=3, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password']

    def validate(self, attr):
        email_exists = User.objects.filter(email=attr['email']).exists()
        username_exists = User.objects.filter(
            username=attr['username']).exists()

        #password = attr['password']----------> this line gives us access to the password#

        if email_exists:
            raise ValidationError("Email has already been used")
        if username_exists:
            raise ValidationError('username has already been taken')
        return super().validate(attr)

    def create(self, validate_data):
        password = validate_data.pop('password')
        user = super().create(validate_data)
        user.set_password(password)
        user.save()
        return user


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name',
                  'last_name', 'phone', 'address', 'picture']


class passwordUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['old_password', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError({'password': 'password fields do not match'})
        return attrs

    def update(self, instance, validate_data):
        instance.set_password(validate_data['password'])
        instance.save()
        return instance
