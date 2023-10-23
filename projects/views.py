from projects.models import Profile
from rest_framework import viewsets
from projects.serializer import (
    ProfileReadOnlySerializer,
    ProfileWriteSerializer,
    ProfileByIdSerializer,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer = ProfileReadOnlySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ["read"]:
            return ProfileReadOnlySerializer
        return ProfileWriteSerializer