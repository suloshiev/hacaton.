from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.views import ObtainAuthToken
from account.serializers import LoginSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from account.serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class RegisterApiView(APIView):
    '''Регистрация'''
    def post(self, request):
        data = request.data
        serializers = RegisterSerializer(data=data)

        if serializers.is_valid(raise_exception=True):
            serializers.save()
            massage = 'Вы успешкно зарегистрировались! Вам придет сообщение с поддверждением!'
            return Response(massage, status=201)


class ActivationView(APIView):
    '''Получение кода активаци'''
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'msg': 'Успешно'}, status=200)
        except User.DoesNotExist:
            return Response({'msg': 'Неверный код!'}, status=400)



class loginApiView(ObtainAuthToken):
    '''Логин'''
    serializer_class = LoginSerializer


class ChangePasswordView(APIView):
    '''Смена пароля'''
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializers = ChangePasswordSerializer(data=request.data,
                                               context={'request': request})
        serializers.is_valid(raise_exception=True)
        serializers.set_new_password()
        return Response('Пароль успешно обнавлен!')




class ForgotPasswordView(APIView):
    '''Вастоновление пароля'''
    def post(self, request):
        data = request.data
        serializer = ForgotPasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.send_code()
        return Response('Вам отправлено письмо для восстановления пароля')


class ForgotPasswordComplete(APIView):
    '''Подтверждение нового пароля'''
    def post(self, request):
        data = request.data
        serializer = ForgotPasswordCompleteSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.set_new_pass()
        return Response('Окей! пороль поменял!')



def login(request):
    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'home.html')