from .models import students
from rest_framework import viewsets, permissions
from .serializers import studentsSerializer

class studentsViewSet(viewsets.ModelViewSet):
    queryset = students.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class = studentsSerializer