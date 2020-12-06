from django.shortcuts import render
from django.shortcuts import redirect
from .models import StudentModel, CourseModel, AttendanceModel, AssignmentModel
from .serializers import StudentSerializer, CourseSerializer, AttendanceSerializer, AssignmentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.db.models import Count

from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView


def index(request):
    return render(request, 'Navigationbar1.html')
def home(request):
    return render(request, 'Navigationbar2.html')

class StudentTable(APIView):
    def get(self, request):
        obj = StudentModel.objects.all()
        # obj_dict = {}
        # for i in obj:
        #     obj_dict['Stdid'] = i.Stdid
        #     obj_dict['Stdname'] = i.Stdname
        #     obj_dict['Email'] = i.Email
        #     obj_dict['course_id'] = i.course_id.course
        serializer = StudentSerializer(obj, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentUpdateDelete(APIView):
    def get_object(self, pk):
        try:
            return StudentModel.objects.get(pk=pk)
        except StudentModel.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        obj = self.get_object(pk)
        serializer = StudentSerializer(obj)
        return Response(serializer.data)
    def put(self, request, pk):
        obj = self.get_object(pk)
        serializer = StudentSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CourseView(APIView):
    def get(self, request):
        obj = CourseModel.objects.all()
        serializer = CourseSerializer(obj, many=True)
        return Response(serializer.data)

# def students_by_course(request):
#     obj = CourseModel.objects.all().annotate(nstudents = Count('studentmodel__stdid'))
#     print(obj)
#     return render(request, 'students_by_course.html', {'obj':obj})

class AttendanceView(APIView):
    def get(self, request):
        obj = AttendanceModel.objects.all()
        serializer = AttendanceSerializer(obj, many=True)
        return Response(serializer.data)

class AssignmentView(APIView):
    def get(self, request):
        obj = AssignmentModel.objects.all()
        serializer = AssignmentSerializer(obj, many=True)
        return Response(serializer.data)

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return redirect('login')


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return redirect(home)

