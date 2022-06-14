from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, generics
from .models import UserDetails
from .serializers import RegistrationSerializer
from rest_framework import status


# Create your views here.


class registrationAPIView(viewsets.ModelViewSet):
    http_method_names = ('post', 'get')
    serializer_class = RegistrationSerializer
    queryset = UserDetails.objects.all()

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

