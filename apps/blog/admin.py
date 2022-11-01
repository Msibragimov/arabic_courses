from django.contrib import admin

from .models import Course, Pricing

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')

@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ('monthly_cost', 'per_week', 'lesson_duration')
