from rest_framework import serializers
from .models import registeronline

class RegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = registeronline
		fields = ('id', 'name', 'lastname', 'ci', 'phone', 'email', 'course', 'contact')