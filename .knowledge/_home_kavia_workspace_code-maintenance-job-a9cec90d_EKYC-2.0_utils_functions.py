{
  "is_source_file": true,
  "format": "Python",
  "description": "This file contains utility functions for facial image processing, including face detection with MTCNN, face padding, and transformation for deep learning models.",
  "external_files": [
    "facenet/models/mtcnn"
  ],
  "external_methods": [
    "facenet.models.mtcnn.MTCNN.detect"
  ],
  "published": [
    "padding_face",
    "extract_face",
    "face_transform",
    "get_image"
  ],
  "classes": [],
  "methods": [
    {
      "name": "padding_face",
      "description": "Pads a bounding box by a specified amount or scale factor."
    },
    {
      "name": "extract_face",
      "description": "Detects and extracts the largest face from an image using MTCNN, with optional padding."
    },
    {
      "name": "face_transform",
      "description": "Preprocesses a face image for input into deep learning models, with model-specific parameters."
    },
    {
      "name": "get_image",
      "description": "Loads an image from file and converts it to RGB format."
    }
  ],
  "calls": [
    "facenet.models.mtcnn.MTCNN.detect",
    "cv.resize",
    "cv.imread",
    "cv.cvtColor"
  ],
  "search-terms": [
    "face detection",
    "MTCNN",
    "face padding",
    "face preprocessing",
    "image loading",
    "deep learning face models"
  ],
  "state": 2,
  "file_id": 17,
  "knowledge_revision": 57,
  "git_revision": "d1e36568fc828d61f29ebe58995c7a10be68814c",
  "ctags": [],
  "filename": "/home/kavia/workspace/code-maintenance-job-a9cec90d/EKYC-2.0/utils/functions.py",
  "hash": "702c2ebebe2620aa14002d0898d897f7",
  "format-version": 4,
  "code-base-name": "https://github.com/DarssiniRamesh/EKYC-2.0.git:main",
  "revision_history": [
    {
      "57": "d1e36568fc828d61f29ebe58995c7a10be68814c"
    }
  ]
}