from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Instructor, Course, Lesson
from .serializers import InstructorSerializer, CourseSerializer, LessonSerializer
from rest_framework import status
from rest_framework import generics



class InstructorAPIView(APIView):

    def get(self, request):
        instructor = Instructor.objects.all()
        serializers = InstructorSerializer(instructor, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializer = InstructorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InstructorUpdateView(generics.UpdateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

    def get_object(self):
        return self.get_queryset().get(pk=self.kwargs['pk'])

class InstructorDeleteView(generics.DestroyAPIView):
    queryset = Instructor.objects.all()

    def get_object(self):
        return self.get_queryset().get(pk=self.kwargs['pk'])



class CourseAPIView(APIView):

    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseUpdateView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_object(self):
        return self.get_queryset().get(pk=self.kwargs['pk'])

class CourseDeleteView(generics.DestroyAPIView):
        queryset = Course.objects.all()

        def get_object(self):
            return self.get_queryset().get(pk=self.kwargs['pk'])



class LessonAPIView(APIView):

    def get(self, request):
        lesson = Lesson.objects.all()
        serializer = LessonSerializer(lesson, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LessonUpdateView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_object(self):
        return self.get_queryset().get(pk=self.kwargs['pk'])


class LessonDeleteView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()

    def get_object(self):
        return self.get_queryset().get(pk=self.kwargs['pk'])