from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.SimpleRouter()

router.register(r'reviewlike' , ReviewsLikeViewSet , basename='review_like')
router.register(r'hashtag' , HashTagViewSet , basename='hashtag')
urlpatterns = [
    path('', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/', UserViewSet.as_view(), name='users'),
    path('post/<int:pk>/edit/' , PostEditViewSet.as_view() , name = 'post_edit'),
    path('post/create/' , PostCreateViewSet.as_view() , name= 'post_create'),
    path('post/' , PostListViewSet.as_view() , name = 'post_list'),
    path('post/<int:pk>/' , PostDetailViewSet.as_view() , name = 'post_detail'),

    path('review/' , ReviewsListViewSet.as_view() , name = 'review'),
    path('review/<int:pk>/' , ReviewsDetailViewSet.as_view() , name = 'review_detail'),
    path('review/<int:pk>/edit/' , ReviewsEditViewSet.as_view() , name='review_edit'),
    path('review/create/' , ReviewsCreateViewSet.as_view() , name = 'review_create'),

    path('message/', MessageListApiView.as_view(), name='message'),
    path('message/<int:pk>/', MessageDetailApiView.as_view(), name='message_detail'),
    path('message/<int:pk>/edit/', MessageEditApiView.as_view(), name='message_edit'),
    path('message/create/', MessageCreateApiView.as_view(), name='message_create'),

    path('chat/', ChatListApi.as_view(), name='chat'),
    path('chat/<int:pk>/', ChatDetailApi.as_view(), name='chat_detail'),
    path('chat/<int:pk>/edit/', ChatEditApi.as_view(), name='chat_edit'),
    path('chat/create/', ChatCreateApi.as_view(), name='chat_create'),

    path('following/', FollowingListAPISet.as_view(), name='following'),
    path('following/<int:pk>/', FollowingDetailAPISet.as_view(), name='following_detail'),
    path('following/<int:pk>/edit/', FollowingEditAPISet.as_view(), name='following_edit'),
    path('following/create/', FollowingCreateAPISet.as_view(), name='following_create'),

    path('archive/', ArchiveListViewSet.as_view(), name='archive'),
    path('archive/<int:pk>/', ArchiveDetailViewSet.as_view(), name='archive_detail'),
    path('archive/<int:pk>/edit/', ArchiveEditViewSet.as_view(), name='archive_edit'),
    path('archive/create/', ArchiveCreateViewSet.as_view(), name='archive_create'),

    path('notes/', NotesListSet.as_view(), name='notes'),
    path('notes/<int:pk>/', NotesCreateSet.as_view(), name='notes_detail'),
    path('notes/<int:pk>/edit/', NotesEditSet.as_view(), name='notes_edit'),

    path('postlike/', PostLikeListApi.as_view(), name='postlike'),
    path('postlike/<int:pk>/', PostLikeDetailApi.as_view(), name='postlike_detail'),
    path('postlike/<int:pk>/edit/', PostLikeEditApi.as_view(), name='postlike_edit'),
    path('postlike/create/', PostLikeCreateApi.as_view(), name='postlike_create'),

    path('stories/', StoriesListApi.as_view(), name='stories'),
    path('stories/<int:pk>/', StoriesDetailApi.as_view(), name='stories_detail'),
    path('stories/<int:pk>/edit/', StoriesEditApi.as_view(), name='stories_edit'),
    path('stories/create/', StoriesCreateApi.as_view(), name='stories_create'),

]