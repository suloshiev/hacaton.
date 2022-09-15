from post.tasks import send_post_info
from . models import Post, Contact
from rest_framework import serializers
from user_profile.serializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    comments=CommentSerializer(many=True,read_only=True)
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['likes'] = instance.likes.filter(like=True).count()
        
        rating_res = 0
        for rating in instance.ratings.all():
            rating_res += int(rating.rating)
        try:
            representation['ratings'] = rating_res / instance.ratings.all().count()
        except ZeroDivisionError:
            pass
        return representation

    
    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        print(post)
        send_post_info.delay(validated_data['content'])
        return post


class RatingSerializer(serializers.Serializer):
    rating = serializers.IntegerField(required=True, min_value=1, max_value=5)



class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'
