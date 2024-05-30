from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import generics, permissions, renderers, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
# from rest_framework_api_key.permissions import HasAPIKey

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
# from .permissions import IsOwnerOrReadOnly


class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # permission_classes = [HasAPIKey]
    # permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticated,)
    # permission_classes = [HasAPIKey]
    # permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)


class SnippetDetailAPI(APIView):
    # queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        codes = [snippet.code for snippet in Snippet.objects.filter(owner=request.user)]
        return Response(codes)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
