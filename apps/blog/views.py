from django.shortcuts import get_object_or_404, redirect, render

from apps.customer.models import Customer

from .models import Course


def home(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})


def course_detail(request, slug):
    detail_course = get_object_or_404(Course, slug=slug)
    pricing = detail_course.pricing
    courses = Course.objects.all()
    if request.method == 'POST':
        
        customer, created = Customer.objects.get_or_create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            phone_number=request.POST['phone_number'],
            course=detail_course
        )
        return redirect('homepage')
    
    return render(request, 'detail_course.html', {'course': detail_course, 'courses': courses, 'pricing': pricing})
