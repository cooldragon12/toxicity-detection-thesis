from transformers import BertTokenizer, TFBertModel
import tensorflow as tf
from django.conf import settings

# CACHING THE MODEL
bert_model = TFBertModel.from_pretrained("bert-base-uncased")


def get_model():
    """
    Load the model and tokenizer
    """
    loaded_model = tf.keras.models.load_model(settings.MODEL_DIR, custom_objects={"TFBertModel": bert_model})
    return loaded_model


# CACHING THE TOKENIZER

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")


def tokenize_text(text):
    """
    Tokenize the text using the tokenizer
    """
    tokenized_text = tokenizer.encode(
        text,
        add_special_tokens=True,
        max_length=65,
        padding="max_length",
        return_attention_mask=False,
        return_tensors="tf",
    )
    return tokenized_text


def predict_toxicity_emotion(text, model):
    """
    Predict the sentiment of the text
    """
    tokenized_text = tokenize_text(text)
    prediction = model.predict(tokenized_text)
    return prediction
