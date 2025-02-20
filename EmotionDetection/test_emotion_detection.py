import unittest,json
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test1(self):
        self.assertEqual(emotion_detector("I am glad this happened"), )
        self.assertEqual(emotion_detector("I am really mad about this"), )
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this"), )
        self.assertEqual(emotion_detector("I am so sad about this"), )
        self.assertEqual(emotion_detector("I am really afraid that this will happen"), )

