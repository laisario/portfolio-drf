from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=50)
    github = models.URLField(max_length=500)
    linkedin = models.URLField(max_length=500)
    bio = models.TextField(max_length=500)

    def _str_(self) -> str:
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    github_url = models.URLField(max_length=500)
    keyword = models.TextField(max_length=50)
    key_skill = models.TextField(max_length=50)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="Projects"
    )

    def _str_(self) -> str:
        return self.name
