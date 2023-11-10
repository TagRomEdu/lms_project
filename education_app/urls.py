from django.urls import path

from education_app.apps import EducationAppConfig
from rest_framework.routers import DefaultRouter

from education_app.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView

app_name = EducationAppConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('create_lesson', LessonCreateAPIView.as_view(), name='create_lesson'),
    path('list_lesson', LessonListAPIView.as_view(), name='list_lesson'),
    path('list_lesson/int:<pk>', LessonRetrieveAPIView.as_view(), name='single_lesson'),
    path('update_lesson/int:<pk>', LessonUpdateAPIView.as_view(), name='update_lesson'),
    path('delete_lesson', LessonDestroyAPIView.as_view(), name='delete_lesson'),

] + router.urls
