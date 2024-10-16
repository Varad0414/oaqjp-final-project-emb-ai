import requests
import json

def emotion_detector(text_to_analyze):
    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(URL, json=input_json, headers=header)

    if response.status_code == 200:
        detected_text = response.json()
        if detected_text.get('emotionPredictions'):
            emotions = detected_text['emotionPredictions'][0]['emotion']
            anger = emotions['anger']
            disgust = emotions['disgust']
            fear = emotions['fear']
            joy = emotions['joy']
            sadness = emotions['sadness']
            
            max_emotion = max(emotions, key=emotions.get)
            formatted_dict_emotions = {
                'anger': anger,
                'disgust': disgust,
                'fear': fear,
                'joy': joy,
                'sadness': sadness,
                'dominant_emotion': max_emotion
            }
            return formatted_dict_emotions
        
        return {"error": "No emotion predictions available."} 

    elif response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }
    
    return {"error": response.text}