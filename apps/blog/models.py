from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.core.validators import RegexValidator


User = get_user_model()


class Pricing(models.Model):
    monthly_cost = models.IntegerField()
    per_week = models.IntegerField()
    lesson_duration = models.CharField(max_length=100)


class Course(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='course-img/', default='images/480x270.png', blank=True)
    pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=100, blank=True)
    main_info = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

