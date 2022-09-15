
from user_profile.models import Friend, UserProfile, Comment
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from . permissions import IsOwnerOrReadOnly
from . serializers import CommentSerializer, ProfileSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fielsd = ['gender']
    ordering_fields = ['studies_at', 'lives_in', 'works_at']
    search_fields = ['nik_name']
                         

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    @action(methods=['POST'], detail=True)
    def friend(self, request, pk, *args, **kwargs):
        try:
            friend_object, _ = Friend.objects.get_or_create(owner=request.user, profil_id=pk)
            friend_object.add_delet = not friend_object.add_delet
            friend_object.save()
            print(friend_object.add_delet)
            status = 'Вы добавили в друзья'
            
            if friend_object.add_delet:
                return Response({'status': status})
            status = 'Вы удалили из друзей'
            return Response({'status': status})
        except:
            return Response('Такого профиля нет!')


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)