from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
     # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    output = f"For the given statement, the system response is \
        'anger': {response['anger']}, 'disgust': {response['disgust']}, \
        'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. \
        The dominant emotion is joy {response['dominant_emotion']}"
    return output

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
    