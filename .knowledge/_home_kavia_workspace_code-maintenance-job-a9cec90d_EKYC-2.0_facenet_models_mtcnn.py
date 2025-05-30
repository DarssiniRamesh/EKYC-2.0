{
  "is_source_file": true,
  "format": "Python",
  "description": "This file contains implementation of the MTCNN face detection model, including classes for PNet, RNet, ONet, and the high-level MTCNN module. It defines neural network architectures, loads pretrained weights, and provides face detection and extraction functionalities.",
  "external_files": [
    "../data/pnet.pt",
    "../data/rnet.pt",
    "../data/onet.pt",
    "./utils/detect_face"
  ],
  "external_methods": [
    "detect_face",
    "extract_face"
  ],
  "published": [
    "MTCNN",
    "detect_face",
    "extract_face",
    "fixed_image_standardization"
  ],
  "classes": [
    {
      "name": "PNet",
      "description": "Implementation of the Proposal Network (PNet) component of the MTCNN face detection pipeline."
    },
    {
      "name": "RNet",
      "description": "Implementation of the Refine Network (RNet) component of the MTCNN pipeline."
    },
    {
      "name": "ONet",
      "description": "Implementation of the Output Network (ONet) component, part of the MTCNN face detector."
    },
    {
      "name": "MTCNN",
      "description": "High-level module that loads the pretrained PNet, RNet, and ONet and performs face detection and cropping."
    }
  ],
  "methods": [
    {
      "name": "fixed_image_standardization",
      "description": "Normalizes face images by standardizing pixel values."
    },
    {
      "name": "prewhiten",
      "description": "Preprocessing method for face images before recognition."
    }
  ],
  "calls": [
    "detect_face",
    "extract_face"
  ],
  "search-terms": [
    "MTCNN",
    "PNet",
    "RNet",
    "ONet",
    "mtcnn.py",
    "detect_face",
    "extract_face",
    "face detection",
    "pretrained weights",
    "face cropping"
  ],
  "state": 2,
  "file_id": 11,
  "knowledge_revision": 47,
  "git_revision": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5",
  "ctags": [],
  "filename": "/home/kavia/workspace/code-maintenance-job-a9cec90d/EKYC-2.0/facenet/models/mtcnn.py",
  "hash": "ddcca1e37267bb855bc5e235d805ab9a",
  "format-version": 4,
  "code-base-name": "https://github.com/DarssiniRamesh/EKYC-2.0.git:main",
  "revision_history": [
    {
      "47": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5"
    }
  ]
}