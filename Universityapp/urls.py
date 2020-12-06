from django.urls import path
from .import views
from knox import views as knox_views

urlpatterns = [
    path('index', views.index),
    path('home', views.home),
    #path('students_by_course', views.students_by_course),
    path('students', views.StudentTable.as_view()),
    path('courses', views.CourseView.as_view()),
    path('attendance', views.AttendanceView.as_view()),
    path('assignment', views.AssignmentView.as_view()),
    path('students/<int:pk>', views.StudentUpdateDelete.as_view()),
    path('register', views.RegisterAPI.as_view(), name='register'),
    path('login', views.LoginAPI.as_view(), name='login'),
    path('logout', knox_views.LogoutView.as_view(), name='logout'),
    #path('logoutall', knox_views.LogoutAllView.as_view(), name='logoutall'),
]