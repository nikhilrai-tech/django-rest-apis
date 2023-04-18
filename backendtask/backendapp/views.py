from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Class
from .serializers import ClassSerializer


class ClassAPIView(generics.RetrieveAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


def class_detail(request, pk):
    class_obj = get_object_or_404(Class, pk=pk)
    serializer = ClassSerializer(class_obj)
    return render(request, 'class_detail.html', {'serializer': serializer})
