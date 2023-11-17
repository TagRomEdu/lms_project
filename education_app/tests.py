from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from education_app.models import Course, Lesson, Subscription
from users_app.models import User


class LessonTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@test.ru',
            first_name='Test',
            last_name='Testov'
        )

        self.course = Course.objects.create(
            title='test',
            description='Test course',
            owner=self.user
        )

        self.lesson = Lesson.objects.create(
            title='lesson 1',
            description='Test lesson',
            url='https://www.youtube.com/watch?v=-47Q_ggvggM',
            course=self.course,
            owner=self.user
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):

        """Lesson creation test"""

        data = {
            'title': 'lesson 2',
            'description': 'Test lesson 2',
            'url': 'https://www.youtube.com/watch?v=-47Q_ggvggM',
            'course': 1,
            'owner': 1
        }
        response = self.client.post(
            reverse('education_app:create_lesson'),
            data=data
        )

        self.assertEquals(response.status_code,
                          status.HTTP_201_CREATED
                          )

    def test_list_lesson(self):

        """Lessons viewing test"""

        response = self.client.get(reverse('education_app:list_lesson'))

        self.assertEquals(response.status_code,
                          status.HTTP_200_OK
                          )

    def test_retrieve_lesson(self):

        """A lesson viewing test"""

        response = self.client.get(reverse('education_app:single_lesson', kwargs={'pk': 5}))

        self.assertEquals(response.status_code,
                          status.HTTP_200_OK
                          )

    def test_update_lesson(self):

        """Lesson updating test"""

        data = {
            'title': 'BOOM',
            'description': 'MENYAEM',
            'url': 'https://www.youtube.com/watch?v=-47Q_ggvggM'
        }
        response = self.client.put(
            reverse('education_app:update_lesson', kwargs={'pk': 6}),
            data=data
        )

        wished_answer = {'id': 6, 'title': 'BOOM', 'description': 'MENYAEM', 'preview': None,
                         'url': 'https://www.youtube.com/watch?v=-47Q_ggvggM', 'course': 5, 'owner': 5
                         }

        self.assertEquals(response.status_code,
                          status.HTTP_200_OK
                          )

        self.assertEquals(response.json(),
                          wished_answer
                          )

    def test_delete_lesson(self):

        """Lesson destroying test"""

        response = self.client.delete(
            reverse('education_app:delete_lesson', kwargs={'pk': 3})
        )

        self.assertEquals(response.status_code,
                          status.HTTP_204_NO_CONTENT
                          )


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='test@test.ru',
            first_name='Test',
            last_name='Testov'
        )

        self.course = Course.objects.create(
            title='test',
            description='Test course',
            owner=self.user
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_subscribe_to_course(self):

        """Subscription creating and adding to course test"""

        response = self.client.post('/education/courses/6/subscribe/')
        is_subscribe = Course.objects.all()[0].subscription_set.all().first()

        self.assertEquals(response.status_code,
                          status.HTTP_201_CREATED
                          )

        self.assertTrue(is_subscribe)

    def test_unsubscribe_from_course(self):

        """Subscription deleting test"""

        response = self.client.delete('/education/courses/7/unsubscribe/')
        is_subscribe = Course.objects.all()[0].subscription_set.all().first()

        self.assertEquals(response.status_code,
                          status.HTTP_204_NO_CONTENT
                          )

        self.assertFalse(is_subscribe)
