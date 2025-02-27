import requests # Import the requests library to handle HTTP requests
import json
def emotion_detector(text_to_analyse): # Define a function named emotion_detector that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyse } } # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header) # Send a POST request to the API with the text and headers
    #return response.text # Return the response text from the API
    formatted_response = json.loads(response.text)
    # parsing response according to emotions
    emotion_list=["anger", "disgust", "fear", "joy", "sadness"]
    output = { emotion : formatted_response["emotionPredictions"][0]["emotion"][emotion]
    for emotion in emotion_list
    }
    dominant_emotion = max(output, key=output.get)
    output["dominant_emotion"] = dominant_emotion
    return output

