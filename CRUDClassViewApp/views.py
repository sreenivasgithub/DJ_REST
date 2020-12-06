from django.shortcuts import render
from django.shortcuts import redirect
from .models import EmployeeModel
from .serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer


def index(request):
    return render(request, 'Navigationbar1.html')
def home(request):
    return render(request, 'Navigationbar2.html')

class EmployeeTable(APIView):
    def get(self, request):
        empobj = EmployeeModel.objects.all()
        empserializer = EmployeeSerializer(empobj, many=True)
        return Response(empserializer.data)
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class EmployeeUpdateDelete(APIView):
    def get_object(self, pk):
        try:
            return EmployeeModel.objects.get(pk=pk)
        except EmployeeModel.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        empobj = self.get_object(pk)
        serializer = EmployeeSerializer(empobj)
        return Response(serializer.data)
    def put(self, request, pk):
        empobj = self.get_object(pk)
        serializer = EmployeeSerializer(empobj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        empobj = self.get_object(pk)
        empobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # return Response({
        # "user": UserSerializer(user, context=self.get_serializer_context()).data,
        # "token": AuthToken.objects.create(user)[1]
        # })
        return redirect('login')

from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        #return super(LoginAPI, self).post(request, format=None)
        return redirect('home')

