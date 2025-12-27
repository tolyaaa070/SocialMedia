from xmlrpc.client import FastParser

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
class UserProfile(AbstractUser):
    age = models.IntegerField(null=True , blank=True , validators=[MinValueValidator(18),
                              MaxValueValidator(90)])
    phone_number = PhoneNumberField(null=True , blank=True)
    email = models.EmailField(unique=True)
    user_photo = models.ImageField(null=True , blank=True)
    user_link = models.URLField(null=True ,blank=True)
    bio = models.TextField(null=True, blank=True)
    is_offical = models.BooleanField(default=False)
    close_account = models.BooleanField(default=False)

    date_registered = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.username},{self.last_name},{self.first_name},{self.bio},{self.user_photo},{self.user_link}'


class Following(models.Model):
    following = models.ForeignKey(UserProfile,  on_delete=models.CASCADE , related_name='following')
    follower = models.ForeignKey(UserProfile,  on_delete=models.CASCADE , related_name='follower')
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.follower} , {self.following}'

class HashTag(models.Model):
    hashtag_name = models.CharField(max_length=100)

    def __str__(self):
        return self.hashtag_name


class Post(models.Model):
    hashtag = models.ManyToManyField(HashTag,blank=True, related_name='hashtag')
    description = models.TextField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    people = models.ManyToManyField(UserProfile, blank=True, related_name='people')

    def __str__(self):
        return self.description


class PostContent(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_content')
    content = models.URLField()



class PostLike(models.Model):
    post = models.ForeignKey(Post ,  on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

class Review(models.Model):
    post = models.ForeignKey(Post,  on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(UserProfile , on_delete=models.CASCADE , related_name='user')
    comment = models.TextField()
    parent = models.ForeignKey(UserProfile ,  on_delete=models.CASCADE , related_name='parent')
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.parent} , {self.post}'

class ReviewLike(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

class Notes(models.Model):
    user = models.OneToOneField(UserProfile,null=True , blank=True, on_delete=models.CASCADE)
    music = models.FileField(null=True, blank=True)
    description = models.TextField(null=True , blank=True)
    def __str__(self):
        return f'{self.user} , {self.music}'

class Stories(models.Model):
    user = models.ForeignKey(UserProfile,  on_delete=models.CASCADE)
    content = models.FileField()
    is_active = models.BooleanField()
    def __str__(self):
        return  f'{self.user} , {self.content}'

class Archive(models.Model):
     user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)


class ArchiveItems(models.Model):
     archive = models.ForeignKey(Archive,  on_delete=models.CASCADE)
     stories = models.ForeignKey(Stories,  on_delete=models.CASCADE)
     def  __str__(self):
        return f'{self.archive} , {self.stories}'

class Chat(models.Model):
    person = models.ManyToManyField(UserProfile)
    created_date = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE , related_name='author')
    text = models.TextField(null=True , blank=True)
    image = models.ImageField(upload_to='image/', null=True , blank=True)
    video = models.FileField(upload_to='video/', null=True , blank=True)
    created_date = models.DateTimeField(auto_now_add=True)