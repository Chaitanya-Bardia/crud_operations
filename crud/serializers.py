from django.db.models import fields
from rest_framework import serializers
from .models import student

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ('name', 'surname', 'student_id', 'marks')