from django.contrib.auth.models import User
from django.utils import timezone

from rest_framework import parsers, renderers, viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListCreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.blog.models import Post
from .serializers import CreateUserSerializer, AuthCustomTokenSerializer, UserSerializer, PostSerializer, \
    PostSearchSerializer


class RegisterUserView(CreateAPIView):
    """
    User registration.
    """
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user.save()

        content = {
            'result': 'User created successfully',
        }

        return Response(content)


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (
        parsers.FormParser,
        parsers.MultiPartParser,
        parsers.JSONParser,
    )

    renderer_classes = (renderers.JSONRenderer,)

    def post(self, request):
        serializer = AuthCustomTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        content = {
            'token': str(token.key),
        }

        return Response(content)


class PostList(ListCreateAPIView):
    """
    List all posts, or create a new post.
    """
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    # def list(self, request, *args, **kwargs):
    #     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #     serializer = PostSerializer(posts, many=True)
    #     return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.validated_data['post']
            post.author = request.user
            post.published_date = timezone.now();
            post.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostSearch(APIView):
    """
    Search post by text in title
    """
    serializer_class = PostSearchSerializer

    def post(self, request):
        serializer = PostSearchSerializer(data=request.data)
        serializer.is_valid()
        query = serializer.validated_data['query']
        posts = Post.objects. \
            filter(title__icontains=query). \
            filter(published_date__lte=timezone.now()).\
            order_by('published_date')

        serializerpost = PostSerializer(posts, many=True)
        return Response(serializerpost.data)


class UserProfile(RetrieveAPIView):
    """
    User profile.
    """
    serializer_class = UserSerializer

    def get_object(self):
        user = self.request.user
        return user


class UserPosts(ListAPIView):
    """
    Posts published by user.
    """
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        posts = Post.objects.filter(author__exact=user).order_by('published_date')
        return posts
