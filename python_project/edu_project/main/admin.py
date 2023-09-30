from django.contrib import admin
from .models import Users, Lessons, Products, Access, LessonViews

admin.site.register(Users)
admin.site.register(Lessons)
admin.site.register(Products)
admin.site.register(Access)
admin.site.register(LessonViews)

