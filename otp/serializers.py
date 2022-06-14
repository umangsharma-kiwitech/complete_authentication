from rest_framework import serializers
import validation_message
from otp.models import UserDetails

'''  authentication serializer  '''


class RegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        required=True, min_length=validation_message.CHAR_LIMIT_SIZE['firstname_min'],
        max_length=validation_message.CHAR_LIMIT_SIZE['firstname_max'],
        error_messages=validation_message.VALIDATION['firstname']
    )

    last_name = serializers.CharField(
        required=True, min_length=validation_message.CHAR_LIMIT_SIZE['lastname_min'],
        max_length=validation_message.CHAR_LIMIT_SIZE['lastname_max'],
        error_messages=validation_message.VALIDATION['lastname']
    )

    email = serializers.EmailField(required=True, error_messages=validation_message.VALIDATION['email'])

    username = serializers.CharField(
        min_length=validation_message.CHAR_LIMIT_SIZE['username_min'],
        max_length=validation_message.CHAR_LIMIT_SIZE['username_max'],
        error_messages=validation_message.VALIDATION['username']
    )

    password = serializers.CharField(required=True, style={'input_type': 'password'},
                                     min_length=validation_message.CHAR_LIMIT_SIZE['password_min'],
                                     max_length=validation_message.CHAR_LIMIT_SIZE['password_max'],
                                     error_messages=validation_message.VALIDATION['password'],
                                     write_only=True)

    is_active = serializers.BooleanField(default=False)

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = UserDetails
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password', 'password2', 'is_active')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_email(self, email):
        existing = UserDetails.objects.filter(email=email).first()
        if existing:
            raise serializers.ValidationError("Someone with that email "
                                              "address has already registered. Was it you?")
        return email

    def validate(self, data):
        if not data.get('password') or not data.get('password2'):
            raise serializers.ValidationError("Please enter a password and "
                                              "confirm it.")
        if data.get('password') != data.get('password2'):
            raise serializers.ValidationError("Those passwords don't match.")
        return data

    def create(self, validated_data, password=None):
        user = UserDetails.objects.create(
            username=validated_data['username'],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            password=validated_data["password"],
            is_active=validated_data["is_active"]
        )
        # user.set_password(validated_data['password'])
        user.save()
        return user
