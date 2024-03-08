from rest_framework import serializers
from .utils import get_model, predict_toxicity_emotion


class EmotionSerializer(serializers.Serializer):
    angry = serializers.FloatField()
    disgust = serializers.FloatField()
    happy = serializers.FloatField()
    neutral = serializers.FloatField()
    sad = serializers.FloatField()
    surprise = serializers.FloatField()

    # Sort the fields in the order of the highest value
    def to_representation(self, instance):
        return dict(sorted(instance.items(), key=lambda x: x[1], reverse=True))


class ToxicitySerializer(serializers.Serializer):
    blaming_others = serializers.FloatField()
    cyberbullying = serializers.FloatField()
    gameplay_experience_complaints = serializers.FloatField()
    gamesplaining = serializers.FloatField()
    multiple_discrimination = serializers.FloatField()
    not_toxic = serializers.FloatField()
    sarcasm = serializers.FloatField()

    # Sort the fields in the order of the highest value
    def to_representation(self, instance):
        return dict(sorted(instance.items(), key=lambda x: x[1], reverse=True))


class ClassifySerializer(serializers.Serializer):
    model = get_model()
    chat_text = serializers.CharField(max_length=200, write_only=True, required=True)
    emotion = EmotionSerializer
    toxicity = ToxicitySerializer

    def validate_chat_text(self, value):
        if len(value) > 200:
            raise serializers.ValidationError("Text should be less than 200 characters")

        return value

    def create(self, validated_data):
        emotion, toxicity = predict_toxicity_emotion(validated_data["chat_text"], self.model)
        # convert ndarray to list
        emotion = emotion.tolist()
        toxicity = toxicity.tolist()
        # convert to 1d list
        emotion = {
            "angry": emotion[0][0],
            "disgust": emotion[0][1],
            "happy": emotion[0][2],
            "neutral": emotion[0][3],
            "sad": emotion[0][4],
            "surprise": emotion[0][5],
        }
        toxicity = {
            "blaming_others": toxicity[0][0],
            "cyberbullying": toxicity[0][1],
            "gameplay_experience_complaints": toxicity[0][2],
            "gamesplaining": toxicity[0][3],
            "multiple_discrimination": toxicity[0][4],
            "not_toxic": toxicity[0][5],
            "sarcasm": toxicity[0][6],
        }

        return emotion, toxicity

    def save(self):
        emotion, toxicity = self.create(self.validated_data)
        # use the emotion and toxicity serializer to convert the ndarray to a dictionary
        return self.emotion(emotion).data, self.toxicity(toxicity).data
