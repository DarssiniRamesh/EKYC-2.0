{
  "is_source_file": true,
  "format": "Python",
  "description": "This file is a test script for eye blink detection using a pre-trained MTCNN face detector and a BlinkDetector class. It loads a video, detects faces in each frame, and checks for eye blinking, printing results and displaying the video.",
  "external_files": [
    "facenet/models/mtcnn.py",
    "liveness_detection/blink_detection.py",
    "videos/eye_blink.mov"
  ],
  "external_methods": [
    "MTCNN.detect",
    "cv.VideoCapture",
    "cv.cvtColor",
    "cv.imshow",
    "cv.waitKey"
  ],
  "published": [],
  "classes": [
    {
      "name": "BlinkDetector",
      "description": "A class responsible for detecting eye blinking in images."
    }
  ],
  "methods": [
    {
      "name": "eye_blink",
      "description": "Method of BlinkDetector class that analyzes a frame and face bounding box to determine if a blink occurred."
    }
  ],
  "calls": [
    "MTCNN.detect",
    "cv.VideoCapture",
    "cv.cvtColor",
    "cv.imshow",
    "cv.waitKey",
    "blink_detector.eye_blink"
  ],
  "search-terms": [
    "blink_test",
    "BlinkDetector",
    "eye_blink",
    "facenet",
    "liveness_detection",
    "MTCNN",
    "cv.VideoCapture",
    "video",
    "detect",
    "blink"
  ],
  "state": 2,
  "file_id": 28,
  "knowledge_revision": 62,
  "git_revision": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5",
  "ctags": [],
  "filename": "/home/kavia/workspace/code-maintenance-job-a9cec90d/EKYC-2.0/tests/blink_test.py",
  "hash": "93c1852ef74bdd992e7ed8696b13bee2",
  "format-version": 4,
  "code-base-name": "https://github.com/DarssiniRamesh/EKYC-2.0.git:main",
  "revision_history": [
    {
      "62": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5"
    }
  ]
}