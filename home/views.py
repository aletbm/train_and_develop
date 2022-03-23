from django.shortcuts import render
from courses.models import Course
# Create your views here.


def home(request):
    courses = Course.objects.filter(price__contains=0)
    return render(request, "home/home.html", {"courses": courses})
