from rest_framework import serializers
from snippets import models


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'title',
            'code',
            'language',
        )
        model = models.Snippet
