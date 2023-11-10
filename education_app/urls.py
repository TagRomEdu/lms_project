from education_app.apps import EducationAppConfig
from rest_framework.routers import DefaultRouter

from education_app.views import CourseViewSet

app_name = EducationAppConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [

] + router.urls
