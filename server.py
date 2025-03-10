"""import packages"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """Define the function sent_detector"""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    # Error handling
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    output = f"For the given statement, the system response is"\
        f" 'anger': {response['anger']}, 'disgust': {response['disgust']},"\
        f" 'fear': {response['fear']}, 'joy': {response['joy']} and"\
        f" 'sadness': {response['sadness']}."\
        f" The dominant emotion is {response['dominant_emotion']}"
    return output

@app.route("/")
def render_index_page():
    """# Render the HTML template using render_index_page"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
    