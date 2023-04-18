from rest_framework import serializers
from .models import Class, Lesson, Resource


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['title', 'description', 'resource_type']


class LessonSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(many=True)

    class Meta:
        model = Lesson
        fields = ['title', 'description', 'resources', 'resources_count']


class ClassSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Class
        fields = ['id', 'title', 'description', 'lessons']
