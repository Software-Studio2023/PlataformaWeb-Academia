from rest_framework import serializers
from .models import students

class studentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = ('id', 'name', 'lastname', 'email', 'rol', 'password')

    def create(self, validated_data):
    	userstudents = students(**validated_data)
    	userstudents.set_password(validated_data['password'])
    	userstudents.save()
    	return userstudents