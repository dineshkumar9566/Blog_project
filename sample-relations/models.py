from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Passport(models.Model):
    number = models.CharField(max_length=20)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

class Library(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    visitors = models.ManyToManyField(Person, related_name='libraries')

class Book(models.Model):
    title = models.CharField(max_length=100)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)