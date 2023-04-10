from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,status
from rest_framework.request import Request
from accounts.sieralizer import RegisterSerializer
from django.contrib.auth import authenticate

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
    def post(self,request:Request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email = email,password = password)

        if user is not None:
            response = {
                "message":"login successfully",
                'token' : user.auth_token.key
            }
            return Response(data=response,status=status.HTTP_200_OK)
        else:
            return Response(data={'message':'Invaild email and password'})
    def get(self,request:Request):
        content = {'user':str(request.user),'auth':str(request.auth)}
        return Response(data=content,status=status.HTTP_200_OK)