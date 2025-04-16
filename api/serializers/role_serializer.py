from rest_framework import serializers

from api.models import Permission, Role, User

from .permission_serializer import PermissionSerializer


class RoleSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(read_only=True, many=True)
    permissions_id = serializers.PrimaryKeyRelatedField(
        queryset=Permission.objects.all(), write_only=True, many=True
    )

    created_by_data = serializers.SerializerMethodField(read_only=True)
    updated_by_data = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Role
        fields = (
            "id",
            "name",
            "code_name",
            "permissions",
            "permissions_id",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
            "created_by_data",
            "updated_by_data",
        )
        read_only_fields = (
            "created_at",
            "updated_at",
            "created_by_data",
            "updated_by_data",
        )

    def create(self, validated_data):
        permissions_id = validated_data.pop("permissions_id")

        role = Role.objects.create(**validated_data)
        role.permissions.set(permissions_id)
        return role

    def update(self, instance, validated_data):
        permissions_id = validated_data.pop("permissions_id")

        instance.name = validated_data.get("name", instance.name)
        instance.code_name = validated_data.get("code_name", instance.code_name)

        instance.permissions.clear()
        instance.permissions.set(permissions_id)

        instance.save()

        return instance

    def get_created_by_data(self, obj):
        if not obj.created_by:
            return None

        user = User.objects.get(pk=obj.created_by.id)
        data = {
            "id": user.id,
            "username": user.username,
            "name": user.name,
        }
        return data

    def get_updated_by_data(self, obj):
        if not obj.updated_by:
            return None

        user = User.objects.get(pk=obj.updated_by.id)
        data = {
            "id": user.id,
            "username": user.username,
            "name": user.name,
        }
        return data
