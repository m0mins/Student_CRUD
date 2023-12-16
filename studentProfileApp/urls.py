from django.urls import path
from studentProfileApp import views


app_name='studentProfileApp'
urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.signUP,name='signUp'),
    path('studentDetails/<int:pk>/',views.studentDetails,name='studentDetails'),
    path('studentDelete/<int:pk>/',views.studentDelete,name='studentDelete'),
    path('editStudent/<int:pk>/',views.editStudent,name='editStudent'),
    
]