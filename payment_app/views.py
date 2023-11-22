
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from payment_app.models import Payment
from payment_app.serializers import PaymentSerializer, PaymentCreateSerializer


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentCreateSerializer


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ('paid_course', 'paid_lesson', 'method')
    ordering_fields = ('date',)


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


