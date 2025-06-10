from django.urls import path
from .views import create_student, student_details

urlpatterns = [
    path('student/', create_student, name='create-student'),
    path('student/<int:student_id>/', student_details, name='student-details')
]
