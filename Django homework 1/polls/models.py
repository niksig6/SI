from django.db import models

class Car(models.Model):
    title = models.charField(max_lenght=100)
    body = models.textField(max_lenght = 255)
