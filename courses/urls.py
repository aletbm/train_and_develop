from django.urls import path
from courses import views

urlpatterns = [
    path("", views.courses, name="Courses"),
    path("results/", views.results, name="Results")
]
