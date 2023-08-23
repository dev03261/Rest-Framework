from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'  # You can also specify specific fields: ('first_name', 'last_name', 'date_of_birth', 'grade')
        #field=['name','age']
        #exclude=['id',]
