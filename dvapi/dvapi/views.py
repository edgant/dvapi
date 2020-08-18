from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


class GetToken(APIView):
    """
    GET a valid JWT token to access the API. It won't receive any parameter or password.
    """
    def get(self, request, format=None):
        refresh = RefreshToken.for_user(request.user)

        return Response({
            'access': str(refresh.access_token),
        })
