from rest_framework.response import Response
from rest_framework import viewsets
from .models import UserDetails, userAddresss, userCorrespondenceAddress
from .serializers import RegistrationSerializer, UserAddressSerializer, userCorrespondenceAddressSerializer
from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


# registration view


class registrationAPIView(viewsets.ModelViewSet):
    http_method_names = ('post', 'get')
    serializer_class = RegistrationSerializer
    queryset = UserDetails.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filter_fields = ['first_name', 'last_name']

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "Message": "User created successfully",

                "User": serializer.data}, status=status.HTTP_201_CREATED
            )
        else:

            return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST})


# for user address
class addressAPIView(viewsets.ModelViewSet):
    http_method_names = ('post', 'get')
    serializer_class = UserAddressSerializer
    queryset = userAddresss.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filter_fields = ['house_number']

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "address entered successfully", 'user': serializer.data
            }, status=status.HTTP_201_CREATED
            )
        else:
            return Response({"error": serializer.errors, "status": status.HTTP_201_CREATED})

# for user correspondence address

class correspondenceAddressAPIView(viewsets.ModelViewSet):
    http_method_names = ('post', 'get')
    serializer_class = userCorrespondenceAddressSerializer
    queryset = userCorrespondenceAddress.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filter_fields = ['corres_house_number', 'corres_landmark']

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "address entered successfully", 'user': serializer.data
            }, status=status.HTTP_201_CREATED
            )
        else:
            return Response({"error": serializer.errors, "status": status.HTTP_201_CREATED})
# # creating login view
# class LoginAPIView(viewsets.ModelViewSet):
#     http_method_names = 'post'
#
#     def post(self, request):
#         email = request.data['email']
#         password = request.data['password']
#
#         user = UserDetails.objects.filter(email=email)
#
#         if user is None:
#             raise AuthenticationFailed('user not found')
#
#         if not user.check_password(password):
#             raise AuthenticationFailed('incorrect password')
#
#         return response
