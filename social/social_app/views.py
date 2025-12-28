from django.shortcuts import render
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.views.generic import ListView
from .serializers import *
from rest_framework import generics , status , viewsets
from rest_framework import filters
from .permission import CheckRole , IsArchiveOwner , StoryPermission
from django_filters.rest_framework import DjangoFilterBackend



class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UserListSet(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']
    permission_classes = [CheckRole]

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class UserUpdateSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

class UserDetailSet(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

class HashTagViewSet(viewsets.ModelViewSet):
    queryset = HashTag.objects.all()
    serializer_class = HashTagSerializers
class PostEditViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializers
class PostCreateViewSet(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializers
class PostListViewSet(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostLLSerializers
    paginate_by = 5
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hashtag',]

class PostDetailViewSet(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializers
class PostLIkeViewSet(viewsets.ModelViewSet):
    queryset = PostLike.objects.all()
    serializer_class = PostListSerializers

class ReviewsListViewSet(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
class ReviewsDetailViewSet(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
class ReviewsEditViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
class ReviewsCreateViewSet(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers


class ReviewsLikeViewSet(viewsets.ModelViewSet):
    queryset = ReviewLike.objects.all()
    serializer_class = ReviewsLikeSerializers

class NotesListSet(generics.ListAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializers
class NotesCreateSet(generics.CreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializers
class NotesEditSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializers


class ArchiveViewSet(viewsets.ModelViewSet):
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializers

class ArchiveListViewSet(generics.ListAPIView):
    queryset = ArchiveItems.objects.all()
    serializer_class = ArchiveItemsSerializers
    permission_classes = [IsArchiveOwner]
class ArchiveEditViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArchiveItems.objects.all()
    serializer_class = ArchiveItemsSerializers
class ArchiveDetailViewSet(generics.RetrieveAPIView):
    queryset = ArchiveItems.objects.all()
    serializer_class = ArchiveItemsSerializers
class ArchiveCreateViewSet(generics.CreateAPIView):
    queryset = ArchiveItems.objects.all()
    serializer_class = ArchiveItemsSerializers

class FollowingListAPISet(generics.ListAPIView):
    queryset = Following.objects.all()
    serializer_class = FollowingSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['follower',]
class FollowingDetailAPISet(generics.RetrieveAPIView):
    queryset = Following.objects.all()
    serializer_class = FollowingSerializers
class FollowingEditAPISet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Following.objects.all()
    serializer_class = FollowingSerializers
class FollowingCreateAPISet(generics.CreateAPIView):
    queryset = Following.objects.all()
    serializer_class = FollowingSerializers

class ChatListApi(generics.ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializers
class ChatCreateApi(generics.CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializers
class ChatEditApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializers
class ChatDetailApi(generics.RetrieveAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializers

class MessageListApiView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['text',]

class MessageDetailApiView(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializers
class MessageEditApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializers
class MessageCreateApiView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializers

class StoriesListApi(generics.ListAPIView):
    queryset = Stories.objects.all()
    serializer_class = StoriesSerializers
    permission_classes = [StoryPermission]
class StoriesDetailApi(generics.RetrieveAPIView):
    queryset = Stories.objects.all()
    serializer_class = StoriesSerializers
class StoriesEditApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stories.objects.all()
    serializer_class = StoriesSerializers
class StoriesCreateApi(generics.CreateAPIView):
    queryset = Stories.objects.all()
    serializer_class = StoriesSerializers

class PostLikeListApi(generics.ListAPIView):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializers
class PostLikeDetailApi(generics.RetrieveAPIView):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializers
class PostLikeEditApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializers
class PostLikeCreateApi(generics.CreateAPIView):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializers