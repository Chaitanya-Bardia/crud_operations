from django.urls import path
from .views import create_student,view_student_details,get_student,update_student_partial,delete_student

urlpatterns = [
    path('create/', create_student, name='create-student'),
    path('list/', view_student_details, name='view-student-details'),
    path('get/<int:id>/', get_student, name='get-student'),
    path('update/<int:id>/', update_student_partial, name='patch-student'),
    path('delete/<int:id>/', delete_student, name='delete-student'),
]
