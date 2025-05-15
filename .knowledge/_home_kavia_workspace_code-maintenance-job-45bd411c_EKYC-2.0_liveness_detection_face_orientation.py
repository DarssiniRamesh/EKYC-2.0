{
  "is_source_file": true,
  "format": "Python",
  "description": "This source file contains a class `FaceOrientationDetector` that detects the orientation of a human face in an image based on facial landmarks. It provides methods for calculating angles between vectors and determining if the face is front-facing, turned left, or turned right.",
  "external_files": [
    "torch",
    "numpy"
  ],
  "external_methods": [
    "torch.Tensor.numpy",
    "np.dot",
    "np.linalg.norm",
    "np.arccos",
    "np.degrees",
    "np.round"
  ],
  "published": [],
  "classes": [
    {
      "name": "FaceOrientationDetector",
      "description": "A class for detecting face orientation in images using facial landmarks and vector mathematics."
    }
  ],
  "methods": [
    {
      "name": "__init__",
      "description": "Initializes the detector with a frontal range for face angles."
    },
    {
      "name": "calculate_angle",
      "description": "Calculates the angle in degrees between two vectors, which can be provided as lists, tuples, numpy arrays, or torch tensors."
    },
    {
      "name": "detect",
      "description": "Determines the face orientation (front, left, or right) based on facial landmarks."
    }
  ],
  "calls": [
    "torch.Tensor.numpy",
    "np.array",
    "np.dot",
    "np.linalg.norm",
    "np.arccos",
    "np.degrees",
    "np.round"
  ],
  "search-terms": [
    "face orientation",
    "landmarks",
    "calculate_angle",
    "detect",
    "frontal_range"
  ],
  "state": 2,
  "file_id": 32,
  "knowledge_revision": 68,
  "git_revision": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5",
  "ctags": [],
  "filename": "/home/kavia/workspace/code-maintenance-job-45bd411c/EKYC-2.0/liveness_detection/face_orientation.py",
  "hash": "bc6dcb533811ab4cd4354d454631b3a8",
  "format-version": 4,
  "code-base-name": "https://github.com/DarssiniRamesh/EKYC-2.0.git:main",
  "revision_history": [
    {
      "68": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5"
    }
  ]
}