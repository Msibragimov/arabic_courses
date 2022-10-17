from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.core.validators import RegexValidator


User = get_user_model()


class Course(models.Model):
    name = models.CharField(max_length=50)
    images = models.ImageField(upload_to='images', blank=True)
    info = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Telefon raqamizni quyidagi ko'rinishda kiriting: '+9989999999'. 15 raqamdan oshmasligi kerak.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.full_name
        