from rest_framework import serializers

# from .utils import tokenize_text


class ClassifySerializer(serializers.Serializer):
    chat_text = serializers.CharField(max_length=200)

    # def validate_chat_text(self, value):
    #     if len(value) > 200:
    #         raise serializers.ValidationError("Text should be less than 200 characters")
    #     try:
    #         tokenize_text(value)
    #     except Exception as e:
    #         raise serializers.ValidationError("Unable to tokenize the text")

    #     return value
