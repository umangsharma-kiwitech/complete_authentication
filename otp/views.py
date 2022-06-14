from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import UserDetails
from .serializers import RegistrationSerializer
from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.


class registrationAPIView(viewsets.ModelViewSet):
    http_method_names = ('post', 'get')
    serializer_class = RegistrationSerializer
    queryset = UserDetails.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['first_name', 'last_name']

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

