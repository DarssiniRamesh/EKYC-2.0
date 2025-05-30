{
  "is_source_file": true,
  "format": "Python",
  "description": "Main application script for a facial verification GUI application, involving face detection, emotion recognition, liveness detection, and verification workflows using various models and a PyQt GUI.",
  "external_files": [
    "face_verification",
    "facenet.models.mtcnn",
    "gui.page1",
    "gui.page2",
    "gui.page3",
    "gui.utils",
    "liveness_detection.blink_detection",
    "liveness_detection.emotion_prediction",
    "liveness_detection.face_orientation",
    "utils.functions",
    "verification_models"
  ],
  "external_methods": [
    "* VGGFace2.load_model",
    "* verify",
    "* get_image"
  ],
  "published": [
    "MainWindow"
  ],
  "classes": [
    {
      "name": "MainWindow",
      "description": "Main GUI window class managing facial verification workflow, including camera control, model initialization, and page navigation."
    }
  ],
  "methods": [
    {
      "name": "__init__",
      "description": "Initializes the main window, sets up models, camera, and GUI pages."
    },
    {
      "name": "verify",
      "description": "Performs verification between ID image and verification image using face detection and verification models."
    },
    {
      "name": "switch_page",
      "description": "Switches between different pages of the GUI, controlling camera states and UI components."
    }
  ],
  "calls": [
    "torch.device",
    "MTCNN",
    "VGGFace2.load_model",
    "queue",
    "verify",
    "get_image",
    "cv.VideoCapture",
    "app.exec_"
  ],
  "search-terms": [
    "MainWindow",
    "verify",
    "VGGFace2",
    "face_verification",
    "liveness_detection",
    "camera",
    "PyQt5.QtWidgets",
    "staged_widget"
  ],
  "state": 2,
  "file_id": 4,
  "knowledge_revision": 38,
  "git_revision": "d1e36568fc828d61f29ebe58995c7a10be68814c",
  "ctags": [],
  "filename": "/home/kavia/workspace/code-maintenance-job-a9cec90d/EKYC-2.0/main.py",
  "hash": "52308ecda1530b308d2d4e620fb2cbca",
  "format-version": 4,
  "code-base-name": "https://github.com/DarssiniRamesh/EKYC-2.0.git:main",
  "revision_history": [
    {
      "38": "d1e36568fc828d61f29ebe58995c7a10be68814c"
    }
  ]
}