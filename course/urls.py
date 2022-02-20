from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('course-list', views.Get_Courses, name="course_list"),
    path('course-list/<slug:slug>', views.Get_Course, name="course"),
    path('course-list/<slug:course_slug>/<slug:lesson_slug>', views.AddComment, name="add_comment"),
    path('course-list/<slug:course_slug>/<slug:lesson_slug>/get-comment', views.Get_Comment, name="get_comment"),
    path('category', views.Get_Categories, name="course_cat"),
    
]