from rest_framework import serializers
from .models import StudentModel, CourseModel, AttendanceModel, AssignmentModel
from django.contrib.auth.models import User

class StudentSerializer(serializers.ModelSerializer):
    course_se= serializers.CharField(source='course_id.course', read_only=True)
    class Meta:
        model = StudentModel
        #fields = '__all__'
        fields = ('Stdid', 'Stdname', 'Email', 'course_se')
        #depth = 1
        # if you want exclude use exclude field like
        # exclude = ['name']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    std_name = serializers.CharField(source='student_id.Stdname', read_only=True)
    class Meta:
        model = AttendanceModel
        fields = ('std_name', 'Attendance')

class AssignmentSerializer(serializers.ModelSerializer):
    std_name = serializers.CharField(source='student_id.Stdname', read_only=True)
    class Meta:
        model = AssignmentModel
        fields = ('std_name', 'Assignment', 'status')

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user