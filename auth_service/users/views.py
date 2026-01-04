from rest_framework.views import APIView
from rest_framework.response import Response
from grpc_client.notification_client import NotificationClient


class LoginView(APIView):
    def post(self, request):
        # fake login success
        user_id = 1

        grpc_client = NotificationClient()
        grpc_client.send_welcome_email(
            user_id=user_id,
            email="user@example.com"
        )

        return Response({"message": "User logged in"})
