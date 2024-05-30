from rest_framework import generics
# from rest_framework_api_key.permissions import HasAPIKey

from snippets import models
from . import serializers


class ListSnippets(generics.ListCreateAPIView):
    queryset = models.Snippet.objects.all()
    serializer_class = serializers.SnippetSerializer


class DetailSnippets(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Snippet.objects.all()
    serializer_class = serializers.SnippetSerializer
    # permission_classes = [HasAPIKey]
