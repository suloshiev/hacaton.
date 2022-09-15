from .models import UserProfile, Comment
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = UserProfile
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['owner'] = instance.owner.email
        return rep



class CommentSerializer(serializers.ModelSerializer):
    commented_by = serializers.ReadOnlyField(source='owner.email')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['owner'] = instance.owner.email
        rep['post'] = instance.post.content
        return rep

    class Meta:
        model = Comment
        fields = '__all__'