{
  "is_source_file": true,
  "format": "Python",
  "description": "This file is a test script for face orientation detection, utilizing a face detection model (MTCNN), and plotting landmarks on video frames captured from a webcam.",
  "external_files": [
    "facenet/models/mtcnn.py",
    "liveness_detection/face_orientation.py",
    "utils/plot.py"
  ],
  "external_methods": [
    "MTCNN.detect",
    "FaceOrientationDetector.detect",
    "plot_landmarks_mtcnn"
  ],
  "published": [],
  "classes": [],
  "methods": [],
  "calls": [
    "cv.VideoCapture",
    "cv.cvtColor",
    "model.detect",
    "orientation_detector.detect",
    "plot_landmarks_mtcnn",
    "cv.imshow",
    "cv.waitKey",
    "cv.flip"
  ],
  "search-terms": [
    "face_orientation_test",
    "FaceOrientationDetector",
    "MTCNN",
    "cv.VideoCapture",
    "landmarks",
    "plot_landmarks_mtcnn"
  ],
  "state": 2,
  "file_id": 27,
  "knowledge_revision": 59,
  "git_revision": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5",
  "ctags": [],
  "filename": "/home/kavia/workspace/code-maintenance-job-a9cec90d/EKYC-2.0/tests/face_orientation_test.py",
  "hash": "baf6a3f90f9904ae768d5da665b55d6f",
  "format-version": 4,
  "code-base-name": "https://github.com/DarssiniRamesh/EKYC-2.0.git:main",
  "revision_history": [
    {
      "59": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5"
    }
  ]
}