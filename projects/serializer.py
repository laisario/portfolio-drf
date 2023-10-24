from rest_framework import serializers
from projects.models import (
    Profile,
    Project,
    Certificate,
    CertifyingInstitution,
)


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


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = (
            "id",
            "name",
            "certifying_institution",
            "timestamp",
            "profiles",
        )


class NestedCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ["id", "name", "timestamp"]


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = NestedCertificateSerializer(many=True, required=False)

    class Meta:
        model = CertifyingInstitution
        fields = ["id", "name", "url", "certificates"]

    def create(self, validated_data):
        certificates_data = validated_data.pop("certificates")
        new_certifying_institution = CertifyingInstitution.objects.create(
            **validated_data
        )
        for certificate in certificates_data:
            Certificate.objects.create(
                certifying_institution=new_certifying_institution,
                **certificate,
            )

        return new_certifying_institution
