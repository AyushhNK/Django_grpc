import grpc
import notification_pb2
import notification_pb2_grpc


class NotificationClient:
    def __init__(self):
        self.channel = grpc.insecure_channel("localhost:50052")
        self.stub = notification_pb2_grpc.NotificationServiceStub(self.channel)

    def send_welcome_email(self, user_id, email):
        request = notification_pb2.EmailRequest(
            user_id=user_id,
            email=email
        )

        response = self.stub.SendWelcomeEmail(request)
        return response.success, response.message
