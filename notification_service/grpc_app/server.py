import os
import django
import sys
import grpc
from concurrent import futures


# ✅ ADD PROJECT ROOT TO PYTHON PATH
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# ✅ SET DJANGO SETTINGS MODULE
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "notification_service.settings"
)

# ✅ INITIALIZE DJANGO
django.setup()
# ✅ CORRECT absolute imports
from services.notifications_service import NotificationService
from grpc_app import notification_pb2_grpc


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    notification_pb2_grpc.add_NotificationServiceServicer_to_server(
        NotificationService(), server
    )
    server.add_insecure_port("[::]:50052")
    server.start()
    print("✅ Notification gRPC Server running on port 50052")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
