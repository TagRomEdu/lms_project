import os

import stripe
from rest_framework import serializers

from payment_app.models import Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'


class PaymentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'

    def create(self, validated_data):
        new_payment = Payment.objects.create(**validated_data)

        description = f'Course: {new_payment.paid_course}' if new_payment.paid_course \
            else f'Lesson: {new_payment.paid_lesson}'

        stripe.api_key = os.getenv("STRIPE_API_KEY")
        new_payment.stripe_id = stripe.PaymentIntent.create(
            amount=new_payment.amount,
            currency='usd',
            automatic_payment_methods={"enabled": True},
            description=description
        ).id

        return new_payment
