{
  "is_source_file": true,
  "format": "Python",
  "description": "This file defines a PyQt5 widget class 'MyWidget' that uses QTimer to periodically update the label text; it also initializes the application and runs the event loop.",
  "external_files": [
    "PyQt5.QtWidgets",
    "PyQt5.QtCore",
    "sys"
  ],
  "external_methods": [
    "QWidget.__init__",
    "QLabel.move",
    "QLabel.adjustSize",
    "QTimer.setInterval",
    "QTimer.timeout.connect",
    "QTimer.start",
    "QApplication.__init__",
    "QApplication.exec_",
    "sys.exit",
    "sys.argv"
  ],
  "published": [],
  "classes": [
    {
      "name": "MyWidget",
      "description": "A custom QWidget that updates a label periodically using QTimer."
    }
  ],
  "methods": [
    {
      "name": "__init__",
      "description": "Constructor initializing the widget, label, and timer."
    },
    {
      "name": "update_label_size",
      "description": "Adjusts the label size to fit its content."
    },
    {
      "name": "update_frame",
      "description": "Increments frame count; updates label text after 100 frames."
    }
  ],
  "calls": [
    "super().__init__",
    "self.label.move",
    "self.label.adjustSize",
    "self.timer.setInterval",
    "self.timer.timeout.connect",
    "self.timer.start",
    "self.label.setText",
    "a.show",
    "sys.exit"
  ],
  "search-terms": [
    "PyQt5 widget",
    "QTimer",
    "label update",
    "Python GUI",
    "MyWidget class",
    "PyQt5 QLabel",
    "PyQt5.QtCore.QTimer",
    "update_frame method"
  ],
  "state": 2,
  "file_id": 30,
  "knowledge_revision": 66,
  "git_revision": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5",
  "ctags": [],
  "filename": "/home/kavia/workspace/code-maintenance-job-a9cec90d/EKYC-2.0/test.py",
  "hash": "66a9b5e2939b4f5f0ec2856c5e0983df",
  "format-version": 4,
  "code-base-name": "https://github.com/DarssiniRamesh/EKYC-2.0.git:main",
  "revision_history": [
    {
      "66": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5"
    }
  ]
}