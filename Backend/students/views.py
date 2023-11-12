from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class Login(APIView):

	def post(self, request):
		email = request.data.get('email', None)
		password = request.data.get('password', None)
		userstudents = authenticate(email=email, password=password)

		if userstudents:
			login(request, userstudents)
			return Response(status=status.HTTP_200_OK)

		return Response(status=status.HTTP_404_NOT_FOUND)


