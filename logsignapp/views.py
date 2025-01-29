from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserSignupSerializer, UserLoginSerializer
from rest_framework.permissions import AllowAny


class SignupAPIView(generics.CreateAPIView):
    serializer_class = UserSignupSerializer
    permission_classes = [AllowAny]  # Allow anyone to access this view

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": {
                "username": user.username,
                "email": user.email,
            },
            "message": "User registered successfully"
        }, status=status.HTTP_201_CREATED)

# Login API
class LoginAPIView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]  # Allow anyone to access this view

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
