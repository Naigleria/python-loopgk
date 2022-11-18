from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.response import Response


from .serializers import RegisterSerializer, UserSerializer
from .messages.messages_ok import *
from .messages.messages_error import *

# Create your views here.
class LoginView(generics.GenericAPIView):
  def get():
    data={"msg": "Metodo GET no permitido"}
    return Response(data, status=status.HTTP_405_METHOD_NOT_ALLOWED)

  def post(self, request):
    email=request.data.get("email", None)
    password=request.data.get("password", None)
    
    if email is None or password is None:
      return Response(LOGIN_REQUIRED_FIELDS_ERROR, status.HTTP_400_BAD_REQUEST)
    else:
      user=authenticate(email = email, password=password)
      if user is not None:
        return Response(
          {
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message":LOGIN_OK["msg"]
          }
          , status=status.HTTP_200_OK)
      else:
        return Response(LOGIN_CREDENTIALS_ERROR, status=status.HTTP_401_UNAUTHORIZED)

class SignUpView(generics.GenericAPIView):
  serializer_class=RegisterSerializer
  def post(self, request):
    serializer= self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user=serializer.save()
    return Response(
      {
        "user": UserSerializer(user, context = self.get_serializer_context()).data,
        "message":"Usuario creado exitosamente. Ahora puedes inicar sesión"
      }
    )