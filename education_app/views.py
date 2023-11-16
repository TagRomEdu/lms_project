from rest_framework import viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from education_app.models import Course, Lesson, Subscription
from education_app.paginators import EducationPaginator
from education_app.permissions import IsModerator, IsOwner
from education_app.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes_by_action = {'update': [IsOwner, IsModerator],
                                    'destroy': [IsOwner],
                                    'retrieve': [IsOwner, IsModerator]
                                    }
    pagination_class = EducationPaginator

    def get_permissions(self):
        return [permission() for permission in self.permission_classes_by_action.get(self.action, [IsAuthenticated])]

    @action(detail=True, methods=['post'])
    def subscribe(self, request, *args, **kwargs):
        course = self.get_object()
        Subscription.objects.get_or_create(user=request.user, course=course)
        return Response({'detail': 'Subscription created'}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['delete'])
    def unsubscribe(self, request, *args, **kwargs):
        course = self.get_object()
        Subscription.objects.filter(user=request.user, course=course).delete()
        return Response({'detail': 'Subscription deleted'}, status=status.HTTP_204_NO_CONTENT)


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = EducationPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]
