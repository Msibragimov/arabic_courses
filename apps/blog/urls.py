from django.urls import path

from apps.blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('contact/', views.contact, name='contact'),
    path('course_detail/<slug:slug>/', views.course_detail, name='course_detail'),
]