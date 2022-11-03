from rest_framework.response import Response
from rest_framework.decorators import APIView, permission_classes
from django.contrib.auth import authenticate
from .token import create_jwt
from .serializer import RegisterUser, UpdateUserSerializer, passwordUpdateSerializer
from rest_framework import status
from .models import User
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAdminUser,  IsAuthenticatedOrReadOnly


class CreateUser(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = RegisterUser

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "User Created Successfully",
                'data': serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user = User.objects.all()
        serilizer = UpdateUserSerializer(user, many=True)
        return Response(serilizer.data, status=status.HTTP_200_OK)


class Login(APIView):

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)

        if user is not None:
            tokens = create_jwt(user)

            response = {
                'message': 'login Successfull',
                'user': {'email': str(user.email), 'username': str(user.username), 'first_name': str(user.first_name),
                         'last_name': str(user.last_name), 'phone': str(user.phone), 'address': str(user.address), 'picture': str(user.picture)},
                'tokens': tokens,
            }

            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': "invalid token"})


class UpdateUser(APIView):
    serializer_class = UpdateUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        if user_id == user.id:
            serializer = self.serializer_class(
                data=request.data, instance=user)
            if serializer.is_valid():
                serializer.save()
                return Response(data={'message': "updated"}, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors)

        return Response(data={'message': 'you are not allowed to carryout this operation'}, status=status.HTTP_401_UNAUTHORIZED)


class Get_n_Dele(APIView):
    serializer_class = UpdateUserSerializer
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            serilizer = self.serializer_class(user, many=False)
            return Response(serilizer.data, status=status.HTTP_200_OK)
        except:
            return Response(data={"MESSAGE": "THIS USER DOES NOT EXIST"}, status=status.HTTP_404_NOT_FOUND)

    def delete(sef, request, pk):
        user = User.objects.get(id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdatePassword(APIView):
    serializer_class = passwordUpdateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        old_password = request.data.get('old_password')
        old_password2 = user.password
        if check_password(old_password, old_password2) == True:
            if user_id == user.id:
                serializer = self.serializer_class(
                    data=request.data, instance=user)
                if serializer.is_valid():
                    serializer.save()
                    return Response(data={'message': "updated"}, status=status.HTTP_202_ACCEPTED)
                return Response(serializer.errors)
            return Response(data={'message': 'you are not allowed to carryout this operation'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(data={'password': "old password is not correct "}, status=status.HTTP_406_NOT_ACCEPTABLE)
