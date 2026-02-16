from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    message= serializers.CharField(required=False, allow_blank=True)
    class Meta:
        model = Student
        fields = '__all__'