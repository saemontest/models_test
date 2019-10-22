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


#Две абстракции

class AbsX(models.Model):
    namex = models.CharField(max_length=10, default='XXX')
    class Meta:
        abstract = True

class AbsY(models.Model):
    namey = models.CharField(max_length=10, default='YYY')
    class Meta:
        abstract = True

class AbsSum(AbsX,AbsY):
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'Имя первой абстракции - {self.namex}, Имя второй абстракции - {self.namey}, дата создания - {self.date}'

#Абстракт с методом

class AbsMethod(models.Model):
    named = models.CharField(max_length=50, default='Name AbsMethod class')

    def show(self):
        return print(self.named, '  some abstract text')
    class Meta:
        abstract = True

class AbsMethodExample(AbsMethod):

    name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Имя обьекта - {self.name}, который создан - {self.date}, и имеет абстракцию - {self.named}'


# JSON in models


from django.db import models
from django.contrib.postgres.fields import JSONField


class BookExample(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    detail_text = models.TextField()
    detail_json = JSONField(default=None)  # requires Django-Mysql package

    class Meta:
        managed = True
        db_table = 'book_example'
        verbose_name = 'Book Example'
        verbose_name_plural = 'Book Examples'



#Отношения многие-к-одному
'''

   1  Сколько объектов из B могут относится к объекту A?
   2  Сколько объектов из A могут относиться к объекту из B?

Если на первый вопрос ответ - множество, а на второй - один (или возможно, что ни одного), то вы имеете дело со связью один-ко-многим.

'''

class MovieHouse(models.Model):
    cinema_name = models.CharField(max_length=50)

    def __str__(self):
        return f'Кинотеатр - {self.cinema_name}'

class Screens(models.Model):
    type_screen = models.CharField(max_length=50)
    seats = models.IntegerField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    place = models.ForeignKey(MovieHouse, on_delete=models.CASCADE)

    def __str__(self):
        return f'Экран - {self.type_screen}, имеет {self.seats} мест, находится в {self.place.cinema_name} и стоимость посещения {self.cost} гривен'