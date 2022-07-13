from unicodedata import category
from django.shortcuts import render
from course.models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse, response
from .serializers import *
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.db.models import Q
# Create your views here.

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def Get_Courses(request):
    if request.method == "GET":
        courses = Course.objects.all()
        
        category_id = request.GET.get('category_id', '')

        if category_id:
            courses = Course.objects.filter(categories__in = [int(category_id)])
        
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def Get_LatestCourses(request):
    if request.method == "GET":
        courses = Course.objects.all()[0:8]
        
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)




@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def Get_Course(request, slug):
    course = Course.objects.get(slug=slug)
    course_serializer = CourseDetailSerializer(course)
    lesson_serializer = LessonSerializer(course.lessons.all(), many=True)

    course_data = course_serializer.data

    data = {
        'course': course_data,
        'lessons': lesson_serializer.data
    }

    return Response(data)



@api_view(["GET",])
@authentication_classes([])
@permission_classes([])
def Get_Categories(request):
    if request.method == "GET":
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


@api_view(["POST",])
def AddComment(request, course_slug, lesson_slug):
    if request.method == "POST":
        data = request.data
        name = data.get('name')
        content = data.get('content')

        course = Course.objects.get(slug = course_slug)
        lesson = Lesson.objects.get(slug = lesson_slug)

        Comment.objects.create(lesson = lesson, course = course, name=name, content = content, created_by = request.user)

        return Response({'message':'Comment added successfully'})
       
@api_view(["GET",])
def Get_Comment(request, course_slug, lesson_slug):
    if request.method == "GET":
        lesson = Lesson.objects.get(slug = lesson_slug)
        serializer = CommentSerializer(lesson.comments.all(), many=True)
        return Response(serializer.data)



@api_view(['POST'])
def Search(request):
    if request.method == "POST":
        q = request.data.get('query', '')
        if q:
            try:
                courses = Course.objects.filter(Q(title__icontains=q)| Q(short_description__icontains=q))
            except courses.DoesNotExist:
                return HttpResponse(status=404)
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data)
        else:
            return Response({"courses":[]})
