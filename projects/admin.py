from django.contrib import admin
from projects.models import (
    Profile,
    Project,
    Certificate,
    CertifyingInstitution,
)


# Register your models here.
class CertificateInline(admin.StackedInline):
    model = Certificate


class CertifyingInstitutionAdmin(admin.ModelAdmin):
    inlines = [CertificateInline]


admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Certificate)
admin.site.register(CertifyingInstitution, CertifyingInstitutionAdmin)
