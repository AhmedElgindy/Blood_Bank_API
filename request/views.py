from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status,generics
from django.utils import timezone
from datetime import timedelta
from .models import BloodRequest,Donate
from .sieralizer import BloodRequestSerializer,BloodRequestCreateSerializer,DonateSieralizer,DonateSerializerCreate,DonateSerializerUpdate

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

#delete a blood request 
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def deleteRequest(request,pk):
    try:
        bloodRequest = BloodRequest.objects.get(pk = pk)
    except:
        return  Response({"message":"the id is wrong"})
    bloodRequest.delete()
    return Response({"message":"the blood request has deleted "})

#delete donate
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def deleteDonate(request,pk):
    try:
        donate = Donate.objects.get(pk = pk)
    except:
        return  Response({"message":"the id is wrong "})
    donate.delete()
    return Response({"message":"the donate request has deleted "})

# * this function should list all the blood request by the user 
class UserBloodRequestsView(generics.ListAPIView):
    serializer_class = BloodRequestCreateSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return BloodRequest.objects.filter(user=user)

# * this funciton to list all the blood request 
class BloodRequestListView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = BloodRequestCreateSerializer
    def get_queryset(self):
      
        return BloodRequest.objects.filter(approved = False)
#accepted bloodrequest

class BloodRequestAccepted(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = DonateSerializerCreate
    def get_queryset(self):
       
        return Donate.objects.filter(approved = True)
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



# * this function should list all the blood request by the user 
class UserDonaterequestsView(generics.ListAPIView):
    serializer_class = DonateSerializerCreate
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Donate.objects.filter(user=user)

# * this funciton to list all the blood request 
class DonaterequestListView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = DonateSerializerCreate
    def get_queryset(self):
        today = timezone.now().date()
        return Donate.objects.filter(approved = False)
 
#this function  for adding the blood group

@api_view(['PUT'])
@permission_classes([IsAdminUser])

def update_donation_blood_group(request, pk):
    
    try:
        donation = Donate.objects.get(pk=pk)
    except Donate.DoesNotExist:
        return Response({'message': 'Donation not found'}, status=404)

    if request.method == 'PUT':
        serializer = DonateSerializerUpdate(data=request.data)
        if serializer.is_valid():
            donation.blood_group = serializer.validated_data.get('blood_group')
            donation.approved = True
            donation.save()
            return Response({'message': 'Blood group updated successfully'})
        return Response(serializer.errors, status=400)