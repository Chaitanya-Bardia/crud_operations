from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import student
from .serializers import studentSerializer
# Create your views here.

@api_view(['POST'])
def create_student(request):
    serializer = studentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET', 'PUT', 'PATCH','DELETE'])
def student_details(request,student_id):
    try:
        s = student.objects.get(student_id=student_id)
    except student.DoesNotExist:
        return Response({'error': 'Student not found'})

    if request.method == 'GET':
        serializer = studentSerializer(s)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = studentSerializer(s, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'PATCH':
        serializer = studentSerializer(s, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'DELETE':
        s.delete()