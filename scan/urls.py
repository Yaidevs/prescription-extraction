from django.urls import path
from . import views

urlpatterns = [
    path('extract-prescription/', views.extract_prescription, name='extract_prescription'),
]
