from django.urls import path

from otp.views import registrationAPIView

urlpatterns = [
    path('register/', registrationAPIView, name='register'),
]