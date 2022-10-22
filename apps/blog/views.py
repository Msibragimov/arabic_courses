from django.shortcuts import get_object_or_404, render

from .models import Course


def home(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'detail_course.html', {'course': course})
