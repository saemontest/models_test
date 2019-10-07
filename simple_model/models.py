from django.db import models



class OneExample(models.Model):

    name = models.CharField(max_length=50)
    text = models.TextField()
    number = models.IntegerField()
    exist = models.BooleanField()
    email = models.EmailField()

    def __str__(self):
        return f'Имя обьекта - {self.name}, его почта - {self.email}'


# Create your models here.
