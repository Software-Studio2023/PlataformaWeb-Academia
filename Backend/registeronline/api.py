from .models import registeronline
from rest_framework import viewsets, permissions
from .serializers import RegisterSerializer

class RegisterViewSet(viewsets.ModelViewSet):
	queryset = registeronline.objects.all()
	permissions_classes = [permissions.AllowAny]
	serializer_class = RegisterSerializer