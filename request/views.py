from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status

from .models import BloodRequest
from .sieralizer import BloodRequestSerializer,BloodRequestCreateSerializer

# this for the self
class BloodRequestCreateAPIView(CreateAPIView):
    queryset = BloodRequest.objects.all()
    serializer_class = BloodRequestSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        fname = self.request.user.Fname
        location = self.request.user.location
        serializer.save(user=self.request.user,Fname = fname,location = location),
# this for the other
class BloodRequestCreateManuallyAPIView(CreateAPIView):
    queryset = BloodRequest.objects.all()
    serializer_class = BloodRequestCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
# this function that update approvel to the request
@api_view(["POST"])
@permission_classes([IsAdminUser])
def approved(request,pk):
    try:
        bloodRequest = BloodRequest.objects.get(pk = pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    bloodRequest.approved = True
    bloodRequest.save()
    return Response({"message":"Blood request has succfully updated "})
