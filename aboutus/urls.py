from django.urls import path
from aboutus import views

urlpatterns = [
    path("", views.about_us, name="About_Us")
]