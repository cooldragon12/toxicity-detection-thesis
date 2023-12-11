from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework import status

from .utils import get_model, predict_toxicity_emotion

# from .serializers import ClassifySerializer


# Create your views here.
class ClassifyView(APIView):
    model = get_model()

    def post(self, request):
        try:
            text = request.data.get("chat_text")
            emotion, toxicity = predict_toxicity_emotion(text, self.model)
            return Response({"toxicity": toxicity[0], "emotion": emotion[0]}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
