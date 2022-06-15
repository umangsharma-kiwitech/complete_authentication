from django.urls import path

from otp.views import registrationAPIView, addressAPIView, correspondenceAddressAPIView

urlpatterns = [
    path('register/', registrationAPIView, name='register'),
    path('address/', addressAPIView, name='address'),
    path('address1/',correspondenceAddressAPIView, name='address1')

]
