from django.urls import path
from .views import ClassAPIView, class_detail


urlpatterns = [
    path('api/class/<int:pk>/', ClassAPIView.as_view(), name='class_api'),
    path('class/<int:pk>/', class_detail, name='class_detail'),
]
