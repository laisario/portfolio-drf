from rest_framework import serializers
from projects.models import Profile


class ProfileReadOnlySerializer(serializers.ModelSerializer):
    read_only = True

    class Meta:
        model = Profile
        fields = "__all__"


class ProfileWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ProfileByIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
