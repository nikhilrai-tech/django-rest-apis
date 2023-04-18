from django.db import models


class Class(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return str(self.id)+(self.title)


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    resources_count = models.IntegerField()
    classes = models.ManyToManyField(Class, related_name='lessons')

    def __str__(self) -> str:
        return str(self.id)+(self.description)


class Resource(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    resource_type = models.CharField(max_length=50)
    lessons = models.ManyToManyField(Lesson, related_name='resources')

    
