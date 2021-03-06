from django.urls import path
from .import views
from knox import views as knox_views

urlpatterns = [
    path('', views.index),
    #path('home', views.home),
    path('Emp', views.EmployeeTable.as_view()),
    path('Emp/<int:pk>', views.EmployeeUpdateDelete.as_view()),
    path('register', views.RegisterAPI.as_view(), name='register'),
    path('login', views.LoginAPI.as_view(), name='login'),
    path('logout', knox_views.LogoutView.as_view(), name='logout'),
    #path('logoutall', knox_views.LogoutAllView.as_view(), name='logoutall'),
]