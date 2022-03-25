from django.shortcuts import render
from courses.models import Course, Category
from django.db.models import Q

# Create your views here.


def courses(request):
    cat_python = Category.objects.get(id=1)
    cat_excel = Category.objects.get(id=2)
    cat_wd = Category.objects.get(id=3)
    cat_js = Category.objects.get(id=4)
    cat_ds = Category.objects.get(id=5)
    cat_aws = Category.objects.get(id=6)
    cat_design = Category.objects.get(id=7)
    cursos_py = Course.objects.filter(category=cat_python)
    cursos_excel = Course.objects.filter(category=cat_excel)
    cursos_wd = Course.objects.filter(category=cat_wd)
    cursos_js = Course.objects.filter(category=cat_js)
    cursos_ds = Course.objects.filter(category=cat_ds)
    cursos_aws = Course.objects.filter(category=cat_aws)
    cursos_design = Course.objects.filter(category=cat_design)
    return render(
        request,
        "courses/courses.html",
        {
            "cursos_py": cursos_py,
            "cursos_excel": cursos_excel,
            "cursos_wd": cursos_wd,
            "cursos_js": cursos_js,
            "cursos_ds": cursos_ds,
            "cursos_aws": cursos_aws,
            "cursos_design": cursos_design,
        },
    )


def results(request):
    search = request.POST.get("search")
    category = [entry["category"] for entry in Category.objects.values("category")]
    if search is None:
        search = request.POST.get("category")
        cat_id = 0
        for i, c in enumerate(category):
            if search == c:
                cat_id = i+1
        if cat_id != 0:
            cat = Category.objects.get(id=cat_id)
            cursos = Course.objects.filter(category=cat)
        else:
            cursos = Course.objects.filter(
            Q(title__icontains=search)
            | Q(description__icontains=search)
            | Q(author__icontains=search)
            | Q(price__contains=search)
        )
    else:
        cursos = Course.objects.filter(
            Q(title__icontains=search)
            | Q(description__icontains=search)
            | Q(author__icontains=search)
            | Q(price__contains=search)
        )
    categories = sorted(set([curso.category.all()[0].__str__() for curso in cursos]))
    authors = sorted(set([curso.author for curso in cursos]))
    cant_cursos = len(cursos)
    large_pag = 10
    ratio = cant_cursos / large_pag
    if (ratio) > round(ratio):
        cant_pages = round(ratio) + 1
    else:
        cant_pages = round(ratio)
    cant_pages = [i for i in range(1, cant_pages + 1)]
    return render(
        request,
        "courses/results.html",
        {
            "cursos": cursos,
            "filter": search,
            "categories": categories,
            "authors": authors,
            "cant_pages": cant_pages,
        },
    )

def info_course(request):
    if request.GET["n"]:
        n = request.GET["n"]
        curso = Course.objects.get(id=n)
    return render(request, "courses/info_course.html", {"curso": curso})