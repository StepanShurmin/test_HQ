from django.urls import path
from content.apps import ContentConfig
from .views import ProductListAPIView, LessonListAPIView

app_name = ContentConfig.name

urlpatterns = [
    path('api/products/', ProductListAPIView.as_view(), name='product_list'),
    path('api/products/<int:product_id>/lessons/', LessonListAPIView.as_view(), name='lesson_list'),
]
