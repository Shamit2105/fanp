from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    questions = [
        ('What is your favorite color?','color'),
        ('What is your favorite animal?','animal'),
        ('What is your favorite food?','food'),
        ('What is your favorite movie?','movie'),
        ('What is your favorite book?','book'),
        ('What is your favorite song?','song'),
        ('What is your favorite TV show?','tv_show'),
        ('What is your favorite video game?','video_game'),
        ('What is your favorite sport?','sport'),
        ('What is your favorite hobby?','hobby'),
    ]
    sec_questions = models.CharField(max_length=100, choices=questions, default='color')
    sec_answer = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=50)
    phno = models.CharField(max_length=10)

