from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status,generics
from django.utils import timezone
from datetime import timedelta
from .models import BloodRequest,Donate
from .sieralizer import BloodRequestSerializer,BloodRequestCreateSerializer,DonateSieralizer,DonateSerializerCreate

# this for the self
class BloodRequestCreateAPIView(CreateAPIView):
    queryset = BloodRequest.objects.all()
    serializer_class = BloodRequestSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        fname = self.request.user.Fname
        location = self.request.user.location
        blood_group = self.request.user.blood_group
        serializer.save(user=self.request.user,Fname = fname,location = location,blood_group = blood_group),
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

# * this function should list all the blood request by the user 
class UserBloodRequestsView(generics.ListAPIView):
    serializer_class = BloodRequestSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return BloodRequest.objects.filter(user=user)

# * this funciton to list all the blood request 
class BloodRequestListView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = BloodRequestSerializer
    def get_queryset(self):
        today = timezone.now().date()
        three_months_ago = today - timedelta(days=90)
        return BloodRequest.objects.filter(date_requested__range=[three_months_ago, today])
 
    
#----------------------------------------------------------------------------------------------------------------------------#
class DonateCreateAPIView(CreateAPIView):
    gueryset = Donate.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = DonateSieralizer

    def perform_create(self, serializer):
        fname = self.request.user.Fname
        location = self.request.user.location
        blood_group =self.request.user.blood_group
        serializer.save(user = self.request.user,Fname = fname,location = location,blood_group = blood_group)

class DonateCreateManuallyAPIView(CreateAPIView):
    gueryset = Donate.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = DonateSerializerCreate

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

@api_view(["POST"])
@permission_classes([IsAdminUser])
def approvedDonate(request,pk):
    try:
        donate = Donate.objects.get(pk = pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    donate.approved = True
    donate.save()
    return Response({"message":"donate request has succfully updated "})

# * this function should list all the blood request by the user 
class UserDonaterequestsView(generics.ListAPIView):
    serializer_class = DonateSieralizer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Donate.objects.filter(user=user)

# * this funciton to list all the blood request 
class DonaterequestListView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = DonateSieralizer
    def get_queryset(self):
        today = timezone.now().date()
        three_months_ago = today - timedelta(days=90)
        return Donate.objects.filter(date_requested__range=[three_months_ago, today])
 