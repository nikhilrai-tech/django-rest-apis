from django.contrib import admin
from . models import Class,Lesson,Resource


@admin.register(Class)
class postmodelAdmin(admin.ModelAdmin):
    list_display=["id","title","description"]

@admin.register(Lesson)
class postmodelAdmin(admin.ModelAdmin):
    list_display=["id","title","description","resources_count"]

@admin.register(Resource)
class postmodelAdmin(admin.ModelAdmin):
    list_display=["id","title","description","resource_type"]