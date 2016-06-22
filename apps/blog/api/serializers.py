from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _

from rest_framework import serializers

from apps.blog.models import Post


class CreateUserSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']

        if User.objects.filter(email=email).count():
            msg = _('User already exist.')
            raise ValidationError(msg)

        user = User(
            username=email,
            email=email,
            first_name=attrs['first_name'],
            last_name=attrs['last_name'],
        )

        user.set_password(password)

        attrs['user'] = user
        return attrs


class AuthCustomTokenSerializer(serializers.Serializer):
    email_or_username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email_or_username = attrs.get('email_or_username')
        password = attrs.get('password')

        if email_or_username and password:
            # Check if user sent email
            if self.validate_email(email_or_username):
                user_request = get_object_or_404(
                    User,
                    email=email_or_username,
                )

                email_or_username = user_request.username

            user = authenticate(username=email_or_username, password=password)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise ValidationError(msg)
            else:
                msg = _('Unable to log in with provided credentials.')
                raise ValidationError(msg)
        else:
            msg = _('Must include "email or username" and "password"')
            raise ValidationError(msg)

        attrs['user'] = user
        return attrs

    def validate_email(self, email):
        from django.core.validators import validate_email
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'date_joined', )


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'text', )

    def validate(self, attrs):
        post = Post(
            title=attrs['title'],
            text=attrs['text'],
        )

        attrs['post'] = post
        return attrs


class PostSearchSerializer(serializers.Serializer):
    query = serializers.CharField()
