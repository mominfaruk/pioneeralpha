from django.db import models


class Directory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TodoTask(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
    directory = models.ForeignKey(Directory, on_delete=models.CASCADE)
    is_important = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.name
