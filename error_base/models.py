from django.db import models
from users.models import CustomUser


class AppModel(models.Model):
    name = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ErrorModel(models.Model):
    type = models.CharField(max_length=255)
    message = models.TextField()
    stack_trace = models.TextField()
    date = models.DateTimeField()
    app_id = models.ForeignKey(AppModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.type
