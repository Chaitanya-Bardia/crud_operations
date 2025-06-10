from django.db.models import fields
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name', 'surname', 'student_id', 'marks']
    
    def validate(self,data):
        if data['marks'] <= 60:
            raise serializers.ValidationError("Marks Should be Greater than 60 to create a student")
        return data