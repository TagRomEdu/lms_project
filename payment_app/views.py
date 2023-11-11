from django.shortcuts import render
from rest_framework import generics

from payment_app.models import Payment
from payment_app.serializers import PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
