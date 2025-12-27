from rest_framework import serializers
from .models import *

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
class UserProfileCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username']

class FollowingSerializers(serializers.ModelSerializer):
    following = UserProfileCreateSerializers()
    follower = UserProfileCreateSerializers()
    created_date = serializers.DateTimeField(format='%d-%m-%y , %H:%M')
    class Meta:
        model=Following
        fields = ['follower' , 'following' , 'created_date']

class HashTagSerializers(serializers.ModelSerializer):
    class Meta:
        model= HashTag
        fields = ['hashtag_name']

class ReviewSerializers(serializers.ModelSerializer):
    user = UserProfileCreateSerializers()
    parent = UserProfileCreateSerializers()
    created_date = serializers.DateTimeField(format='%d-%m-%y , %H:%M')
    class Meta:
        model = Review
        fields = ['post' , 'user' , 'comment' ,'parent' , 'created_date']

class ReviewPostSerializers(serializers.ModelSerializer):
    user = UserProfileCreateSerializers()
    created_date = serializers.DateTimeField(format='%d-%m-%y , %H:%M')
    class Meta:
        model = Review
        fields = [ 'user' , 'comment' , 'created_date']
class PostContentSerializers(serializers.ModelSerializer):
    class Meta:
        model= PostContent
        fields = ['content']
class PostListSerializers(serializers.ModelSerializer):
    reviews = ReviewPostSerializers(many=True)
    post_content = PostContentSerializers(many=True)
    created_date = serializers.DateTimeField(format ='%d-%m-%y , %H:%M')
    people = UserProfileCreateSerializers(many=True)
    hashtag = HashTagSerializers(many=True)
    author = UserProfileCreateSerializers()

    class Meta:
        model = Post
        fields = ['id','hashtag','description','created_date', 'author' , 'post_content','people','reviews']

class PostLLSerializers(serializers.ModelSerializer):
    reviews = ReviewSerializers(many=True)
    post_content = PostContentSerializers(many=True)
    author = UserProfileCreateSerializers()
    created_date = serializers.DateTimeField(format ='%d-%m-%y , %H:%M')
    hashtag = HashTagSerializers(many=True)
    class Meta:
        model = Post
        fields = ['id','author' ,'hashtag', 'post_content','reviews','created_date']

class PostLikeSerializers(serializers.ModelSerializer):
    class Meta:
        model= PostLike
        fields = '__all__'


class ReviewsLikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReviewLike
        fields = '__all__'

class NotesSerializers(serializers.ModelSerializer):
    user = UserProfileCreateSerializers()
    class Meta:
        model = Notes
        fields = ['user' , 'music' , 'description']

class StoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stories
        fields = '__all__'
class ArchiveItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ArchiveItems
        fields = '__all__'
class ChatSerializers(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d-%m-%y , %H:%M')
    person = UserProfileCreateSerializers(many=True)
    class Meta:
        model= Chat
        fields = ['person' , 'created_date']
class MessageSerializers(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d-%m-%y , %H:%M')
    chat = ChatSerializers()
    author = UserProfileCreateSerializers()
    class Meta:
        model = Message
        fields =[ 'created_date' , 'chat' , 'author' , 'text' ,'image' ,'video']
