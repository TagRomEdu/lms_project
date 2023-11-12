from rest_framework import serializers

from education_app.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons(self, obj):
        if obj.lesson_set.all():
            lesson_list = [lesson.title for lesson in obj.lesson_set.all()]
            return lesson_list
        return 'There are no lessons in the course'

    def get_lessons_count(self, obj):
        return obj.lesson_set.count()
