from rest_framework import serializers

from education_app.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.IntegerField(source='lesson_set.count', required=False)
    lessons = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons(self, obj):
        if obj.lesson_set.all():
            lesson_list = [lesson.title for lesson in obj.lesson_set.all()]
            return lesson_list
        return 'There are no lessons in the course'


