from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Instructor, Course, Lesson


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ('id','name','email','specialty')

    def validate_email(self, email):
        if Instructor.objects.filter(email=email).exists():
            raise serializers.ValidationError("Bu email manzili allaqachon mavjud.")
        return email

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('title', 'description', 'instructor', 'start_date', 'end_date')

    def validate(self, non_field_errors):
        start_date = non_field_errors.get('start_date')
        end_date = non_field_errors.get('end_date')

        if not start_date or not end_date:
            raise serializers.ValidationError("Boshlanish va tugash sanalari kiritilishi shart.")
        if start_date >= end_date:
            raise serializers.ValidationError("Kursning boshlanish sanasi tugash sanasidan oldin bo'lishi kerak.")
        return non_field_errors

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'content', 'course', 'order')

    def validate_order(self, order):
        if order < 0:
            raise ValidationError("Tartib raqami musbat butun son bo'lishi kerak.")
        return order