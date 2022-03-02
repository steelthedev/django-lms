from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title','course','status','lesson_type']
    list_filter = ['status', 'lesson_type']
    search_fields = ['title', 'short_description', 'long_description']

admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Comment)