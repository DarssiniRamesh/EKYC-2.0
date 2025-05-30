{
  "is_source_file": true,
  "format": "Python",
  "description": "This source file implements facial verification functions including face matching, face verification, and main execution logic. It relies on models, distance metrics, and image processing utilities to compare two face images and determine if they match.",
  "external_files": [
    "facenet/models/mtcnn.py",
    "utils/distance.py",
    "utils/functions.py",
    "verification_models.py"
  ],
  "external_methods": [
    "Cosine_Distance",
    "L1_Distance",
    "Euclidean_Distance",
    "findThreshold",
    "face_transform",
    "extract_face",
    "get_image"
  ],
  "published": [
    "face_matching",
    "verify"
  ],
  "classes": [],
  "methods": [
    {
      "name": "face_matching",
      "description": "Performs face matching using a specified distance metric and model, returning True if faces match within a threshold."
    },
    {
      "name": "verify",
      "description": "Verifies if two face images belong to the same person by detecting faces and comparing embeddings."
    }
  ],
  "calls": [
    "model.device()",
    "face_transform()",
    "model()",
    "findThreshold()",
    "extract_face()",
    "get_image()",
    "VGGFace2.load_model()"
  ],
  "search-terms": [
    "face_verification",
    "face_matching",
    "VGG-Face2",
    "MTCNN",
    "distance_metrics",
    "face detection",
    "face comparison"
  ],
  "state": 2,
  "file_id": 3,
  "knowledge_revision": 37,
  "git_revision": "d1e36568fc828d61f29ebe58995c7a10be68814c",
  "ctags": [],
  "filename": "/home/kavia/workspace/code-maintenance-job-a9cec90d/EKYC-2.0/face_verification.py",
  "hash": "de634f5134979c7308d6d85c27a41a5c",
  "format-version": 4,
  "code-base-name": "https://github.com/DarssiniRamesh/EKYC-2.0.git:main",
  "revision_history": [
    {
      "37": "d1e36568fc828d61f29ebe58995c7a10be68814c"
    }
  ]
}