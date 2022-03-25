from django.shortcuts import render
from courses.models import Course

# Create your views here.


def home(request):
    courses = Course.objects.filter(price__contains=0)
    return render(request, "home/home.html", {"courses": courses})


def error404(request, exception=None):
    title = "Page Not Found"
    msj = "The page you want to access does not exist"
    status = "404"
    return render(
        request,
        "home/errors.html",
        context={"title": title, "msj": msj, "status": status},
        status=404,
    )

def error500(request, exception=None):
    title = "Server Error"
    msj = "Try again later"
    status = "500"
    return render(
        request,
        "home/errors.html",
        context={"title": title, "msj": msj, "status": status},
        status=500,
    )
