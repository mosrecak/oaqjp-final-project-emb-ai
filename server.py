from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("__name__")

@app.route('/')
def render_index_page():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    
    if not text_to_analyze:
        return {"message": "Invalid input parameter"}, 422
    
    emotions = {}
    emotions = emotion_detector(text_to_analyze)
    response = json.loads(emotions)
    
    if response:
        return {"message": response}, 200

    return {"message": "An error occured with your request"}, 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)