{
  "is_source_file": true,
  "format": "Python",
  "description": "This Python source file implements a challenge-response system for face and emotion recognition, including challenge generation, response validation using models for emotion, face orientation, and blinking detection, and real-time video processing with OpenCV.",
  "external_files": [
    "facenet/models/mtcnn.py",
    "liveness_detection/blink_detection.py",
    "liveness_detection/emotion_prediction.py",
    "liveness_detection/face_orientation.py",
    "utils/functions.py"
  ],
  "external_methods": [
    "facenet.models.mtcnn.MTCNN",
    "liveness_detection.blink_detection.BlinkDetector.eye_blink",
    "liveness_detection.emotion_prediction.EmotionPredictor.predict",
    "liveness_detection.face_orientation.FaceOrientationDetector.detect",
    "utils.functions.extract_face"
  ],
  "published": [
    "random_challenge",
    "get_question",
    "get_challenge_and_question",
    "result_challenge_response"
  ],
  "classes": [],
  "methods": [
    {
      "name": "random_challenge",
      "description": "Selects a random challenge from predefined options ('smile', 'surprise', 'blink eyes', 'right', 'left')."
    },
    {
      "name": "get_question",
      "description": "Generates a question or instruction based on the provided challenge."
    },
    {
      "name": "get_challenge_and_question",
      "description": "Picks a random challenge and generates the corresponding question or instruction."
    },
    {
      "name": "result_challenge_response",
      "description": "Processes a video frame to evaluate if the user's response matches the challenge, utilizing face detection and various models."
    }
  ],
  "calls": [
    "random.choice",
    "random.randint",
    "extract_face",
    "cv.cvtColor",
    "cv.flip",
    "cv.putText",
    "cv.imshow",
    "cv.waitKey",
    "cv.VideoCapture"
  ],
  "search-terms": [
    "challenge_response",
    "face_orientation",
    "blink_detection",
    "emotion_prediction",
    "MTCNN",
    "real-time face challenge"
  ],
  "state": 2,
  "file_id": 2,
  "knowledge_revision": 40,
  "git_revision": "d1e36568fc828d61f29ebe58995c7a10be68814c",
  "ctags": [],
  "filename": "/home/kavia/workspace/code-maintenance-job-a9cec90d/EKYC-2.0/challenge_response.py",
  "hash": "e8ba73b6750f446370a8fac24685dd9f",
  "format-version": 4,
  "code-base-name": "https://github.com/DarssiniRamesh/EKYC-2.0.git:main",
  "revision_history": [
    {
      "40": "d1e36568fc828d61f29ebe58995c7a10be68814c"
    }
  ]
}