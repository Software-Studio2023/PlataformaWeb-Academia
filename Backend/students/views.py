from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import students

class SignIn(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')           

        if email is None or password is None:
            return Response({'error': 'Please, supply username and password'}, status=status.HTTP_400_BAD_REQUEST)      
       
        try:
            userstudents = students.objects.get(email=email)
            if userstudents.check_password(password):
                refresh = RefreshToken.for_user(userstudents)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Credentials incorrect'}, status=status.HTTP_401_UNAUTHORIZED)
        except students.DoesNotExist:
            return Response({'error': 'Credentials incorrect'}, status=status.HTTP_401_UNAUTHORIZED)