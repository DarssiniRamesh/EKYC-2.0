{
  "is_source_file": true,
  "format": "Python",
  "description": "This source file defines a PyQt5 QWidget subclass 'IDCardPhoto' which provides a GUI interface for selecting and displaying an image of an ID card. The widget includes buttons for selecting an image file, navigating to the next page, and exiting, as well as label elements and image display functionalities.",
  "external_files": [
    "PyQt5.QtCore",
    "PyQt5.QtGui",
    "PyQt5.QtWidgets",
    "./utils"
  ],
  "external_methods": [
    "add_button"
  ],
  "published": [
    "IDCardPhoto"
  ],
  "classes": [
    {
      "name": "IDCardPhoto",
      "description": "A QWidget subclass providing interface for selecting and displaying an ID card photo, with navigation and control buttons."
    }
  ],
  "methods": [
    {
      "name": "__init__",
      "description": "Initializes the IDCardPhoto widget, configuring window properties, labels, buttons, and internal state."
    },
    {
      "name": "switch_page",
      "description": "Calls the main window method to switch to the specified page index."
    },
    {
      "name": "rescale_image",
      "description": "Calculates scaled width and height for displaying the selected image, maintaining aspect ratio based on a fixed height of 400 pixels."
    },
    {
      "name": "selectImage",
      "description": "Opens a file dialog for the user to select an image file, then loads and displays the selected image within the widget, enabling the 'Next' button."
    },
    {
      "name": "clear_window",
      "description": "Hides the displayed image, resetting the display area."
    }
  ],
  "calls": [
    "QFileDialog.getOpenFileName",
    "cv.imread",
    "self.next.setDisabled",
    "self.main_window.switch_page",
    "pixmap.scaled"
  ],
  "search-terms": [
    "IDCardPhoto",
    "selectImage",
    "PyQt5",
    "QFileDialog",
    "cv2",
    "image selection",
    "widget layout",
    "image display"
  ],
  "state": 2,
  "file_id": 23,
  "knowledge_revision": 63,
  "git_revision": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5",
  "ctags": [],
  "filename": "/home/kavia/workspace/code-maintenance-job-a9cec90d/EKYC-2.0/gui/page1.py",
  "hash": "62f340aa7774fc965745ee425c15b5c4",
  "format-version": 4,
  "code-base-name": "https://github.com/DarssiniRamesh/EKYC-2.0.git:main",
  "revision_history": [
    {
      "63": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5"
    }
  ]
}