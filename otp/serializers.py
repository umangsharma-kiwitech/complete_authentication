from rest_framework import serializers
import validation_message
from otp.models import UserDetails, userAddresss, userCorrespondenceAddress


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


# for user address

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = userAddresss
        fields = ('id', 'house_number', 'landmark', 'country', 'state', 'city', 'pincode', 'user')

    user = serializers.PrimaryKeyRelatedField(queryset=UserDetails.objects.all())

    house_number = serializers.CharField(required=True, max_length=validation_message.CHAR_LIMIT_SIZE['house_max'],
                                         error_messages=validation_message.ADDRESS['house_number']
                                         )

    landmark = serializers.CharField(required=True, max_length=validation_message.CHAR_LIMIT_SIZE['landmark_max'],
                                     error_messages=validation_message.ADDRESS['landmark'])

    country = serializers.CharField(required=True, max_length=validation_message.CHAR_LIMIT_SIZE['country_max'],
                                    error_messages=validation_message.ADDRESS['country'])

    state = serializers.CharField(required=True, max_length=validation_message.CHAR_LIMIT_SIZE['state_max'],
                                  error_messages=validation_message.ADDRESS['state'])

    city = serializers.CharField(required=True, max_length=validation_message.CHAR_LIMIT_SIZE['city_max'],
                                 error_messages=validation_message.ADDRESS['city'])

    pincode = serializers.IntegerField(required=True,
                                       error_messages=validation_message.ADDRESS['pincode'])

    def create(self, validated_data):
        user = userAddresss.objects.create(
            user=validated_data['user'],
            house_number=validated_data['house_number'],
            landmark=validated_data['landmark'],
            country=validated_data['country'],
            state=validated_data['state'],
            city=validated_data['city'],
            pincode=validated_data['pincode']
        )
        user.save()
        return user

    def validate_UserAddress(self, user):
        existing = userAddresss.objects.filter(user=user).first()
        if existing:
            raise serializers.ValidationError("You have already added an address")
        return user

    def validate_house_number(self, house_number):
        if not house_number:
            raise serializers.ValidationError("Please enter house number")
        return house_number

    def validate_landmark(self, landmark):
        if not landmark:
            raise serializers.ValidationError("Please enter suitable landmark")
        return landmark

    def validate_country(self, country):
        if not country:
            raise serializers.ValidationError("Please enter suitable landmark")
        return country

    def validate_state(self, state):
        if not state:
            raise serializers.ValidationError("Please enter your state")
        return state

    def validate_city(self, city):
        if not city:
            raise serializers.ValidationError("Please enter city")
        return city

    def validate_pincode(self, pincode):
        if not pincode:
            raise serializers.ValidationError("Please enter pincode")
        return pincode


# for user correspondence address

class userCorrespondenceAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = userCorrespondenceAddress
        fields = ('id', 'corres_house_number', 'corres_landmark', 'country1', 'state1', 'city1', 'pincode1')

    corres_house_number = serializers.CharField(required=True,
                                                max_length=validation_message.CHAR_LIMIT_SIZE['corres_house_max'],
                                                error_messages=validation_message.CORRESPONDENCE_ADDRESS['house_number']
                                                )

    corres_landmark = serializers.CharField(required=True,
                                            max_length=validation_message.CHAR_LIMIT_SIZE['corres_landmark_max'],
                                            error_messages=validation_message.CORRESPONDENCE_ADDRESS['corres_landmark']
                                            )

    country1 = serializers.CharField(required=True, max_length=validation_message.CHAR_LIMIT_SIZE['country_max'],
                                     error_messages=validation_message.ADDRESS['country'])

    state1 = serializers.CharField(required=True, max_length=validation_message.CHAR_LIMIT_SIZE['state_max'],
                                   error_messages=validation_message.ADDRESS['state'])

    city1 = serializers.CharField(required=True, max_length=validation_message.CHAR_LIMIT_SIZE['city_max'],
                                 error_messages=validation_message.ADDRESS['city'])

    pincode1 = serializers.IntegerField(required=True,
                                       error_messages=validation_message.ADDRESS['pincode'])

    def create(self, validated_data):
        user = userCorrespondenceAddress.objects.create(
            corres_house_number=validated_data['corres_house_number'],
            corres_landmark=validated_data['corres_landmark'],
            country1=validated_data['country1'],
            state1=validated_data['state1'],
            city1=validated_data['city1'],
            pincode1=validated_data['pincode1']
        )
        user.save()
        return user

    def validate_corres_house_number(self, corres_house_number):
        if not corres_house_number:
            raise serializers.ValidationError("Please enter house number")
        return corres_house_number

    def validate_corres_landmark(self, corres_landmark):
        if not corres_landmark:
            raise serializers.ValidationError("Please enter suitable landmark")
        return corres_landmark

    def validate_country1(self, country1):
        if not country1:
            raise serializers.ValidationError("Please enter suitable landmark")
        return country1

    def validate_state1(self, state1):
        if not state1:
            raise serializers.ValidationError("Please enter your state")
        return state1

    def validate_city1(self, city1):
        if not city1:
            raise serializers.ValidationError("Please enter city")
        return city1

    def validate_pincode1(self, pincode1):
        if not pincode1:
            raise serializers.ValidationError("Please enter pincode")
        return pincode1
