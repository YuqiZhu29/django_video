from django.urls import path
from .views.base import Index

urlpatterns = [
    path('index', Index.as_view())
]