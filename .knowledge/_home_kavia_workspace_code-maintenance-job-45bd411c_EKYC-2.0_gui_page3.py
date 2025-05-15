{
  "is_source_file": true,
  "format": "Python",
  "description": "This file implements a graphical user interface dialog for challenge-response verification, utilizing camera input for face recognition and challenge questions, built with PyQt5 framework.",
  "external_files": [
    "./utils",
    "challenge_response"
  ],
  "external_methods": [
    "add_button",
    "get_challenge_and_question",
    "result_challenge_response"
  ],
  "published": [
    "ChallengeWindow"
  ],
  "classes": [
    {
      "name": "ChallengeWindow",
      "description": "A PyQt5 dialog class that manages a challenge-response verification process involving real-time camera feed and questions."
    }
  ],
  "methods": [
    {
      "name": "__init__",
      "description": "Initializes the ChallengeWindow with camera and model parameters, sets up UI components, and challenge data."
    },
    {
      "name": "rescale_image",
      "description": "Returns the dimensions to which the camera image should be scaled."
    },
    {
      "name": "update_camera",
      "description": "Captures a frame from the camera, processes it, updates the display, and manages challenge response logic."
    },
    {
      "name": "back_switch_page",
      "description": "Switches the main window to a different page."
    },
    {
      "name": "closeEvent",
      "description": "Releases camera resources and stops the timer when the window is closed."
    },
    {
      "name": "open_camera",
      "description": "Starts the camera feed and updates on a timer interval."
    },
    {
      "name": "close_camera",
      "description": "Stops the camera update timer."
    },
    {
      "name": "clear_window",
      "description": "Resets challenge state and clears UI elements."
    },
    {
      "name": "update_challenge_label",
      "description": "Updates the challenge instruction label with text, question, or coordinates."
    }
  ],
  "calls": [
    "cv.flip",
    "cv.cvtColor",
    "QPixmap.fromImage",
    "get_challenge_and_question",
    "result_challenge_response",
    "add_button"
  ],
  "search-terms": [
    "ChallengeWindow",
    "face recognition",
    "PyQt5 dialog",
    "challenge response",
    "camera feed",
    "QTimer"
  ],
  "state": 2,
  "file_id": 24,
  "knowledge_revision": 60,
  "git_revision": "bd3f4853bd4feb7735d719c09988b377d4169026",
  "ctags": [],
  "filename": "/home/kavia/workspace/code-maintenance-job-45bd411c/EKYC-2.0/gui/page3.py",
  "hash": "ca038c6ce7edbada631c1370da08dd74",
  "format-version": 4,
  "code-base-name": "https://github.com/DarssiniRamesh/EKYC-2.0.git:main",
  "revision_history": [
    {
      "60": "bd3f4853bd4feb7735d719c09988b377d4169026"
    }
  ]
}