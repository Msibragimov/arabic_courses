from django.urls import path

from apps.blog import views


urlpatterns = [
    path('', views.home, name='homepage'),
    path('course_detail/<slug:slug>/', views.course_detail, name='course_detail'),
]