'''Demo Flask app for emotion detection'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detector():
    '''Demo method for emotion detection'''
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    dominant_emotion = emotions['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again"

    response = f"""For the given statement, the system response is
    'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}.
    The dominant emotion is <strong>{dominant_emotion}</strong>."""
    return response,200

@app.route("/")
def render_index_page():
    '''Demo index page'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    