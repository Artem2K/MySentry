from django.db import models


class AppModel(models.Model):
    name = models.CharField(max_length=255)
    token = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ErrorModel(models.Model):
    type = models.CharField(max_length=255)
    message = models.TextField()
    stack_trace = models.TextField()
    date = models.DateTimeField()
    app_id = models.ForeignKey(AppModel, on_delete= models.CASCADE)

    def __str__(self):
        return self.type
