from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import BloodRequest
from .sieralizer import BloodRequestSerializer


class BloodRequestCreateAPIView(CreateAPIView):
    queryset = BloodRequest.objects.all()
    serializer_class = BloodRequestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)