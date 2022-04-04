from pyexpat import model
from statistics import mode
from datetime import datetime
from django.db import models
from django.conf import settings

class Subject(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, default="")
    field = models.CharField(max_length=200, default="")

    def __str__(self):
        return f"{self.name}"

User = settings.AUTH_USER_MODEL

class Skills(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)
    current_level = models.IntegerField(default=1)
    required_level = models.IntegerField(default=1)
    last_updated = models.DateField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self}"

    def get_user_name(self):
        return self.user.username

    def get_subject_name(self):
        return self.subject.name