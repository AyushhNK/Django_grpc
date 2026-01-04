from grpc_app import notification_pb2, notification_pb2_grpc

class NotificationService(notification_pb2_grpc.NotificationServiceServicer):

    def SendWelcomeEmail(self, request, context):
        print(f"📧 Sending email to {request.email}")

        return notification_pb2.EmailResponse(
            success=True,
            message="Email sent successfully"
        )
