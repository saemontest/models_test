from django.db import models



class OneExample(models.Model):

    name = models.CharField(max_length=50)
    text = models.TextField()
    number = models.IntegerField()
    exist = models.BooleanField()
    email = models.EmailField()

    def __str__(self):
        return f'Имя обьекта - {self.name}, его почта - {self.email}'


#Абстрактная модель

class AbsMain(models.Model):
    point = models.CharField(max_length=10, default='ABS')

    class Meta:
        abstract = True

class AbsExample(AbsMain):

    name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Имя обьекта - {self.name}, который создан - {self.date}, и имеет абстракцию - {self.point}'


# Наследование другой моделью

class FirstModel(models.Model):
    name = models.CharField(max_length=10, default='MainFirstModel')

class SecondModel(models.Model):
    named = models.ForeignKey(FirstModel, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Имя обьекта - {self.named.__class__} и {self.named}, его дата создания - {self.date}'


#Миксуем


class AbsMain(models.Model):
    abs = models.CharField(max_length=10, default='abstract')
    class Meta:
        abstract = True

class MixOne(AbsMain):
    name = models.CharField(max_length=50, default='MixOne')
    date = models.DateTimeField(auto_now=True)

class MixTwo(models.Model):
    named = models.ForeignKey(MixOne, on_delete=models.CASCADE)

    def __str__(self):
        return f'Имя обьекта - {self.named}, который создан - {self.named.date}, и имеет абстракцию - {self.named.abs}'