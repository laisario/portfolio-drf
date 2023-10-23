from rest_framework import serializers
from projects.models import Profile, Project


class ProfileReadOnlySerializer(serializers.ModelSerializer):
    read_only = True

    class Meta:
        model = Profile
        fields = "__all__"


class ProfileWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ProjectReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class ProjectWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
