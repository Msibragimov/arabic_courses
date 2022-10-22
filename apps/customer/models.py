from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Telefon raqamizni quyidagi ko'rinishda kiriting: '+9989999999'. 15 raqamdan oshmasligi kerak.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    email = models.EmailField(blank=True)

    bio = models.TextField(max_length=800, null=True, blank=True)
    profile_photo = models.ImageField(upload_to='images/', default='avatar.png', blank=True)