from django.contrib import admin
from .models import Person, Passport, Library, Book

admin.site.register(Person)
admin.site.register(Passport)
admin.site.register(Library)
admin.site.register(Book)