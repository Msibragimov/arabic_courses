from django.shortcuts import get_object_or_404, render

from .models import Course, Contact


def home(request):
    courses = Course.objects.all()
    return render(request, 'homepage.html', {'courses': courses})


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'detail_course.html', {'course': course})


def contact(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts.html', {'contacts': contacts})