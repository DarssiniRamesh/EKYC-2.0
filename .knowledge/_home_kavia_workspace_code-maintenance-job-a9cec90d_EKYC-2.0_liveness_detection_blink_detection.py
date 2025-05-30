{
  "is_source_file": true,
  "format": "Python",
  "description": "This file contains a Python class `BlinkDetector` that uses dlib and OpenCV to detect eye blinks in facial images, including methods for facial landmark detection, eye aspect ratio calculation, and blink detection logic.",
  "external_files": [
    "landmarks/shape_predictor_68_face_landmarks.dat"
  ],
  "external_methods": [
    "dlib.shape_predictor",
    "dlib.rectangle",
    "cv.cvtColor",
    "face_utils.shape_to_np",
    "math.dist"
  ],
  "published": [],
  "classes": [
    {
      "name": "BlinkDetector",
      "description": "A class for detecting eye blinking in facial images"
    }
  ],
  "methods": [
    {
      "name": "__init__",
      "description": "Initializes the BlinkDetector, loads the facial landmarks predictor model, and sets blink detection thresholds."
    },
    {
      "name": "eye_blink",
      "description": "Detects eye blinking within a face region of an input image by calculating the eye aspect ratio and counting blinks."
    },
    {
      "name": "eye_aspect_ratio",
      "description": "Calculates the eye aspect ratio based on eye landmarks to determine if the eyes are closed."
    }
  ],
  "calls": [
    "dlib.shape_predictor",
    "dlib.rectangle",
    "cv.cvtColor",
    "face_utils.shape_to_np",
    "math.dist"
  ],
  "search-terms": [
    "BlinkDetector",
    "eye_blink",
    "face_utils.FACIAL_LANDMARKS_IDXS",
    "shape_predictor_68_face_landmarks.dat",
    "eye_aspect_ratio",
    "blink detection",
    "dlib",
    "cv2",
    "opencv",
    "blinking detection"
  ],
  "state": 2,
  "file_id": 33,
  "knowledge_revision": 69,
  "git_revision": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5",
  "ctags": [],
  "filename": "/home/kavia/workspace/code-maintenance-job-a9cec90d/EKYC-2.0/liveness_detection/blink_detection.py",
  "hash": "5f392045a7d2044c46e72aa4feeb13fd",
  "format-version": 4,
  "code-base-name": "https://github.com/DarssiniRamesh/EKYC-2.0.git:main",
  "revision_history": [
    {
      "69": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5"
    }
  ]
}