from django.shortcuts import get_object_or_404, render
from projects.models import (
    Profile,
    Project,
    Certificate,
    CertifyingInstitution,
)
from rest_framework import viewsets
from projects.serializer import (
    ProfileReadOnlySerializer,
    ProfileWriteSerializer,
    ProjectReadOnlySerializer,
    ProjectWriteSerializer,
    CertificateSerializer,
    CertifyingInstitutionSerializer,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer = ProfileReadOnlySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        if request.method == "GET":
            profile = get_object_or_404(Profile, pk=kwargs.get("pk"))
            # kwargs.get("pk")
            # profile = self.get_object()
            print('>>>>>>>>>>>', profile, '<<<<<<<<<<<<<<<<<<<<<')
            return render(request, "profile_detail.html", {"profile": profile})
        return super().retrieve(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action in ["read"]:
            return ProfileReadOnlySerializer
        return ProfileWriteSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer = ProjectReadOnlySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ["read"]:
            return ProjectReadOnlySerializer
        return ProjectWriteSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class CertifyingInstitutionViewSet(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
