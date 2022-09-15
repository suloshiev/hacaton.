
from .serializers import ContactSerializer, PostSerializer, RatingSerializer
from .models import Contact, Post, Like, Rating, Favorite
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from user_profile.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet



class LargeResultSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'parm_size'
    max_page_size = 10000


class PostViewSet(viewsets.ModelViewSet):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    pagination_class = LargeResultSetPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    '''Функция для добавления Лайка'''
    @action(methods=['POST'], detail=True)
    def like(self, request, pk, *args, **kwargs):
        try:
            like_object, _ = Like.objects.get_or_create(owner=request.user, post_id=pk)
            print(like_object)
            print(pk)
            like_object.like = not like_object.like
            print(like_object.like)
            like_object.save()
            status = 'Вы поставили Like'

            if like_object.like:
                return Response({'status': status})
            status = 'Вы удалили Like'
            return Response({'status': status})
        except:
            return Response('Нет такого поста!')

    '''Функция для добавления рейтинга'''
    @action(methods=['POST'], detail=True)
    def rating(self, request, pk, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj, _ = Rating.objects.get_or_create(product_id=pk,
                                              owner=request.user)
        obj.rating = request.data['rating']
        obj.save()
        return Response(request.data, status=201)


    '''Функция для добавления или удаления из избранного'''
    @action(methods=['POST'], detail=True)
    def favorit(self, request, pk, *args, **kwargs):
        try:
            favorite_obj, _ = Favorite.objects.get_or_create(owner=request.user, post_id=pk)
            favorite_obj.favorite = not favorite_obj.favorite
            favorite_obj.save()
            status = 'Вы добавили в избранное'

            if favorite_obj.favorite:
                return Response({'status': status})
            status = 'Вы удалили из избранного'
            return Response({'status': status})
        except:
            return Response('Нет такого поста!')



class ContactView(mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]