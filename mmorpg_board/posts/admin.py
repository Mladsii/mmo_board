from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post, Response, Category

# Регистрация моделей
admin.site.register(Post)
admin.site.register(Response)
admin.site.register(Category)