{
  "is_source_file": true,
  "format": "Python",
  "description": "This file defines an emotion detection neural network model based on VGG-Face architecture, including a class for model instantiation, loading pre-trained weights, transforming images, and predicting emotional states from images.",
  "external_files": [
    "landmarks/emotion_weights.pt"
  ],
  "external_methods": [
    "torch.load"
  ],
  "published": [
    "EmotionPredictor",
    "EmotionDetectionModel"
  ],
  "classes": [
    {
      "name": "EmotionDetectionModel",
      "description": "A convolutional neural network based on VGG-Face architecture for emotion classification."
    },
    {
      "name": "EmotionPredictor",
      "description": "A wrapper class that loads the emotion detection model, handles image preprocessing, and makes emotion predictions."
    }
  ],
  "methods": [
    {
      "name": "transform",
      "description": "Preprocesses an input image: resizes, converts to tensor, and normalizes."
    },
    {
      "name": "predict",
      "description": "Predicts the emotion class label from an input image."
    }
  ],
  "calls": [
    "torch.load",
    "os.path.join",
    "Image.fromarray"
  ],
  "search-terms": [
    "EmotionDetectionModel",
    "EmotionPredictor",
    "liveness_detection",
    "emotion_weights.pt",
    "VGG-Face"
  ],
  "state": 2,
  "file_id": 31,
  "knowledge_revision": 67,
  "git_revision": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5",
  "ctags": [],
  "filename": "/home/kavia/workspace/code-maintenance-job-45bd411c/EKYC-2.0/liveness_detection/emotion_prediction.py",
  "hash": "3617587d43cf120f92e9925ed838e25f",
  "format-version": 4,
  "code-base-name": "https://github.com/DarssiniRamesh/EKYC-2.0.git:main",
  "revision_history": [
    {
      "67": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5"
    }
  ]
}