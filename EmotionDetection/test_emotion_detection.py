import unittest,json
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test1(self):
        emotions_response = {}
        emotions_response = emotion_detector("I am glad this happened")
        dominant_emotion = emotions_response.get("dominant_emotion")
        self.assertEqual(dominant_emotion, "joy")
        emotions_response = emotion_detector("I am really mad about this")
        dominant_emotion = emotions_response.get("dominant_emotion")
        self.assertEqual(dominant_emotion, "anger")
        emotions_response = emotion_detector("I feel disgusted just hearing about this")
        dominant_emotion = emotions_response.get("dominant_emotion")
        self.assertEqual(dominant_emotion, "disgust")
        emotions_response = emotion_detector("I am so sad about this")
        dominant_emotion = emotions_response.get("dominant_emotion")
        self.assertEqual(dominant_emotion, "sadness")        
        emotions_response = emotion_detector("I am really afraid that this will happen")
        dominant_emotion = emotions_response.get("dominant_emotion")
        self.assertEqual(dominant_emotion, "fear")    

unittest.main()

