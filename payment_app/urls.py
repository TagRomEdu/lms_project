from django.urls import path

from payment_app.apps import PaymentAppConfig
from payment_app.views import PaymentListAPIView, PaymentCreateAPIView, PaymentRetrieveAPIView

app_name = PaymentAppConfig.name


urlpatterns = [
    path('payment_list/', PaymentListAPIView.as_view(), name='payment_list'),
    path('create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('ayment_list/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payment_retrieve'),
]
