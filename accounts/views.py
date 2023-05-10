from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,status
from rest_framework.request import Request
from accounts.sieralizer import RegisterSerializer
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@api_view(['GET'])
def getData(request):
    content = {'name':'Ahmed'}
    return Response(content)

class SingUp(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self,request:Request):
        data = request.data

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()

            respone = {'message':'your accounte created successfully ',
                       'data': serializer.data }
            
            return Response(data=respone,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST,data=serializer.errors)

class Login(APIView):
    def post(self, request: Request):
        phone_num = request.data.get('phone_num')
        password = request.data.get('password')

        user = authenticate(phone_num=phone_num, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)

            response = {
                "message": "login successfully",
                'token': token.key
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Invalid phone number and password'})

    def get(self, request: Request):
        content = {'user': str(request.user), 'auth': str(request.auth)}
        return Response(data=content, status=status.HTTP_200_OK)
class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request:Request):
        try:
            token = Token.objects.get(user = request.user)
            token.delete()
        except Token.DoesNotExist:
            pass

        return Response(status=status.HTTP_200_OK)
   
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def isadmin(request):
    user = request.user
    is_admin = user.is_superuser
    return Response({is_admin})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    data = {
        'name': user.Fname,
        'phone_num': user.phone_num,
        'email': user.email,
    }
    return Response(data=data,status=status.HTTP_202_ACCEPTED)