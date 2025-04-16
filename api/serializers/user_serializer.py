from rest_framework import serializers

from api.models import Role, User


class UserSerializer(serializers.ModelSerializer):
    role_data = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "name",
            "password",
            "profile_status",
            "profile_image",
            "role",
            "role_data",
        )

        read_only_fields = ("id", "username", "name", "is_delete")
        extra_kwargs = {"password": {"write_only": True}}

    def get_role_data(self, obj):
        if not obj.role:
            return None

        role = Role.objects.get(pk=obj.role.id)
        data = {"id": role.id, "name": role.name, "code_name": role.code_name}
        return data

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    # confirm_password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    email = serializers.EmailField(required=True)
    contact = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'contact', 'password', 'profile_image']
        extra_kwargs = {
            'id': {'read_only': True},
        }

    # def validate(self, attrs):
    #     Validate password and confirm_password match
    #     if attrs.get('password') != attrs.get('confirm_password'):
    #         raise serializers.ValidationError({"confirm_password": "Passwords do not match."})
    #     return attrs

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username is already taken.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already taken.")
        return value

    def create(self, validated_data):
        # Remove confirm_password as it's not part of the model
        # validated_data.pop('confirm_password')
        password = validated_data.pop('password')
        
        # Set default role to "basic"
        try:
            role = Role.objects.get(code_name='basic')
        except Role.DoesNotExist:
            raise serializers.ValidationError({"role": "Default role 'basic' does not exist."})
        
        # Create user
        user = User(**validated_data, role=role)
        user.profile_status = 'Current'
        user.set_password(password)
        user.save()
        return user