from __future__ import print_function # In python 2.7
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("__name__")

@app.route('/')
def render_index_page():
    return render_template('index.html')

@app.route('/emotionDetector')
def detector():
    text_to_analyze = request.args.get('textToAnalyze')
 
    emotions = emotion_detector(text_to_analyze)

    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    dominant_emotion = emotions['dominant_emotion']

    if not text_to_analyze:
        return "Please input a new sentence", 422

    response = f"""For the given statement, the system response is
    'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}.
    The dominant emotion is <strong>{dominant_emotion}</strong>."""
    return response, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)