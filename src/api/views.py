from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ClassifySerializer


# from .serializers import ClassifySerializer


# Create your views here.
class ClassifyView(APIView):
    serializer_class = ClassifySerializer

    def post(self, request):
        try:
            text = request.data.get("chat_text")
            valid_data = self.serializer_class(data={"chat_text": text})
            if valid_data.is_valid(raise_exception=True):
                emotion, toxicity = valid_data.save()
                return JsonResponse({"toxicity": toxicity, "emotion": emotion})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
