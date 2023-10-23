from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=50)
    github = models.URLField(max_length=500)
    linkedin = models.URLField(max_length=500)
    bio = models.TextField(max_length=500)

    def _str_(self) -> str:
        return self.name
