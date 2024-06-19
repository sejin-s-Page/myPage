from django.urls import path
from . import views

urlpatterns = [
    path('', views.ResumeView.as_view()),
]