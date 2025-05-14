{
  "is_source_file": true,
  "format": "Python",
  "description": "This file defines a GUI class VerificationWindow for a face verification process, utilizing PyQt5 for UI elements, OpenCV for camera capture, and custom logic for verification status updates.",
  "external_files": [
    "utils.py"
  ],
  "external_methods": [
    "add_button"
  ],
  "published": [
    "VerificationWindow"
  ],
  "classes": [
    {
      "name": "VerificationWindow",
      "description": "A dialog window that captures video frames from a camera, displays instructions, performs face verification, and manages user interaction via buttons."
    }
  ],
  "methods": [
    {
      "name": "__init__",
      "description": "Initializes the verification window, sets up UI elements, camera access, and callback functions."
    },
    {
      "name": "update_process_label",
      "description": "Updates the label displaying current processing messages."
    },
    {
      "name": "rescale_image",
      "description": "Returns the dimensions for video frame display."
    },
    {
      "name": "update_camera",
      "description": "Captures a frame from the camera, processes it, updates the UI, and performs verification after a number of frames."
    },
    {
      "name": "next_switch_page",
      "description": "Switches to the next page in the main window."
    },
    {
      "name": "back_switch_page",
      "description": "Returns to the previous page in the main window."
    },
    {
      "name": "open_camera",
      "description": "Starts the camera feed updates."
    },
    {
      "name": "close_camera",
      "description": "Stops the camera feed updates."
    },
    {
      "name": "closeEvent",
      "description": "Releases camera resources and stops timers upon window closure."
    },
    {
      "name": "clear_window",
      "description": "Resets UI elements and frame counters."
    }
  ],
  "calls": [
    "cv.flip",
    "cv.cvtColor",
    "QImage",
    "QPixmap.fromImage",
    "self.camera.read",
    "self.camera.release",
    "self.timer.stop",
    "self.timer.timeout.connect",
    "self.timer.start",
    "self.next.setDisabled",
    "self.back",
    "self.update_process_label",
    "self.switch_page"
  ],
  "search-terms": [
    "PyQt5",
    "camera",
    "VerificationWindow",
    "face verification",
    "cv2",
    "QTimer",
    "QLabel",
    "QDialog"
  ],
  "state": 2,
  "file_id": 22,
  "knowledge_revision": 61,
  "git_revision": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5",
  "ctags": [],
  "filename": "/home/kavia/workspace/code-maintenance-job-a9cec90d/EKYC-2.0/gui/page2.py",
  "hash": "da25dbf464da0d5db7561547b7321e21",
  "format-version": 4,
  "code-base-name": "https://github.com/DarssiniRamesh/EKYC-2.0.git:main",
  "revision_history": [
    {
      "61": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5"
    }
  ]
}