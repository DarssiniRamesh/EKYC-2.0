{
  "is_source_file": true,
  "format": "Python",
  "description": "This file is a test script for emotion prediction in video frames using face detection and emotion classification models. It captures video from a webcam, detects faces, predicts emotions, and displays the results frame-by-frame.",
  "external_files": [
    "facenet/models/mtcnn.py",
    "liveness_detection/emotion_prediction.py",
    "utils/functions.py",
    "utils/plot.py"
  ],
  "external_methods": [
    "facenet.models.mtcnn.MTCNN",
    "liveness_detection.emotion_prediction.EmotionPredictor.predict",
    "utils.functions.extract_face",
    "cv2.VideoCapture",
    "cv2.cvtColor",
    "cv2.putText",
    "cv2.imshow",
    "cv2.waitKey",
    "cv2.flip"
  ],
  "published": [],
  "classes": [],
  "methods": [],
  "calls": [
    "cv2.VideoCapture",
    "cv2.cvtColor",
    "extract_face",
    "emotion_predictor.predict",
    "cv.putText",
    "cv.imshow",
    "cv.waitKey",
    "cv.flip"
  ],
  "search-terms": [
    "emotion_test",
    "MTCNN",
    "EmotionPredictor",
    "face detection",
    "emotion prediction",
    "webcam",
    "cv2"
  ],
  "state": 2,
  "file_id": 29,
  "knowledge_revision": 64,
  "git_revision": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5",
  "ctags": [],
  "filename": "/home/kavia/workspace/code-maintenance-job-a9cec90d/EKYC-2.0/tests/emotion_test.py",
  "hash": "e12c9c1a79775ef8aa4556025f7459b1",
  "format-version": 4,
  "code-base-name": "https://github.com/DarssiniRamesh/EKYC-2.0.git:main",
  "revision_history": [
    {
      "64": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5"
    }
  ]
}