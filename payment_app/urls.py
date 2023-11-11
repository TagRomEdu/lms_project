from django.urls import path

from payment_app.apps import PaymentAppConfig
from payment_app.views import PaymentListAPIView

app_name = PaymentAppConfig.name


urlpatterns = [
    path('payment_list/', PaymentListAPIView.as_view(), name='payment_list')
]
