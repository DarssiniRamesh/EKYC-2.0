{
  "is_source_file": true,
  "format": "Python",
  "description": "This file contains utility functions and core detection logic for detecting faces within images using a multi-stage neural network approach (likely MTCNN), including functions for image preprocessing, bounding box generation, non-max suppression, and face extraction.",
  "external_files": [
    "torch",
    "torch.nn.functional",
    "torchvision.transforms.functional",
    "torchvision.ops.boxes",
    "PIL.Image",
    "numpy",
    "os",
    "math",
    "cv2",
    "opencv-python",
    "optional dependency"
  ],
  "external_methods": [
    "interpolate",
    "batched_nms",
    "imresample",
    "save_img",
    "get_size",
    "crop_resize",
    "extract_face"
  ],
  "published": [
    "detect_face",
    "extract_face",
    "imresample",
    "save_img",
    "get_size",
    "crop_resize",
    "rerec",
    "bbreg",
    "generateBoundingBox",
    "nms_numpy",
    "batched_nms_numpy"
  ],
  "classes": [],
  "methods": [
    {
      "name": "fixed_batch_process",
      "description": "Processes batches of images through a model with a fixed batch size to prevent memory overload and concatenates the results."
    },
    {
      "name": "detect_face",
      "description": "Main function that detects faces in images by constructing image pyramids, applying three-stage neural network processing, bounding box regression, and non-max suppression. Returns bounding boxes and facial landmarks for each image in the batch."
    },
    {
      "name": "bbreg",
      "description": "Applies bounding box regression adjustments to refine detected boxes."
    },
    {
      "name": "generateBoundingBox",
      "description": "Generates candidate bounding boxes from network outputs based on thresholded probabilities and regression data."
    },
    {
      "name": "nms_numpy",
      "description": "Performs non-max suppression on boxes and scores to eliminate overlapping detections, using method 'Min' or default."
    },
    {
      "name": "batched_nms_numpy",
      "description": "Performs batched non-max suppression across multiple classes or groups in detection boxes."
    },
    {
      "name": "pad",
      "description": "Calculates padding to ensure bounding boxes stay within image boundaries."
    },
    {
      "name": "rerec",
      "description": "Converts bounding boxes to square shape while maintaining the center."
    },
    {
      "name": "imresample",
      "description": "Resizes images or image tensors to a specified size using interpolation."
    },
    {
      "name": "crop_resize",
      "description": "Crops and resizes an image or numpy array based on a bounding box and target size."
    },
    {
      "name": "save_img",
      "description": "Saves an image to disk, supporting both numpy array and PIL image formats."
    },
    {
      "name": "get_size",
      "description": "Returns the size of an image or tensor in width and height."
    },
    {
      "name": "extract_face",
      "description": "Extracts a face region from a PIL Image given a bounding box, with optional margin and saving capabilities. Returns a face tensor."
    }
  ],
  "search-terms": [
    "detect_face",
    "facenet",
    "multi-stage detection",
    "bounding box regression",
    "face extraction",
    "nms",
    "mtcnn",
    "face detection pipeline"
  ],
  "state": 2,
  "file_id": 7,
  "knowledge_revision": 43,
  "git_revision": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5",
  "ctags": [],
  "filename": "/home/kavia/workspace/code-maintenance-job-a9cec90d/EKYC-2.0/facenet/models/utils/detect_face.py",
  "hash": "90a264eaaae95fef2cf44b12e4ec47ca",
  "format-version": 4,
  "code-base-name": "https://github.com/DarssiniRamesh/EKYC-2.0.git:main",
  "revision_history": [
    {
      "43": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5"
    }
  ]
}