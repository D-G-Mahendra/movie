from django.contrib import admin

# Register your models here.
from .models import Movie,Director,Genre

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Director)