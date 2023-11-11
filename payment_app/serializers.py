from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers
from rest_framework.filters import OrderingFilter

from payment_app.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        filter_backends = [OrderingFilter, DjangoFilterBackend]
        filterset_fields = ('paid_course', 'paid_letter', 'method')
        ordering_fields = ('date',)
