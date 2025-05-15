{
  "is_source_file": true,
  "format": "Python",
  "description": "This file defines a utility function `download_url_to_file` for downloading files from a URL, with features like progress display, hash verification, and temporary file handling.",
  "external_files": [
    "hashlib",
    "os",
    "shutil",
    "sys",
    "tempfile",
    "urllib.request"
  ],
  "external_methods": [
    "urllib.request.urlopen",
    "urllib.request.Request"
  ],
  "published": [
    "download_url_to_file"
  ],
  "classes": [
    {
      "name": "tqdm",
      "description": "A fallback dummy tqdm class that provides a minimal interface for progress bar functionality when the actual tqdm library is not installed."
    }
  ],
  "methods": [
    {
      "name": "download_url_to_file",
      "description": "Downloads a file from a URL to a specified local path, optionally verifies its SHA256 hash prefix, and displays a progress bar."
    }
  ],
  "calls": [
    "urllib.request.urlopen",
    "urllib.request.Request",
    "hashlib.sha256",
    "os.path.expanduser",
    "os.path.dirname",
    "shutil.move",
    "os.path.exists",
    "os.remove"
  ],
  "search-terms": [
    "download_url",
    "file download function",
    "hash verification",
    "progress bar download",
    "Python file download utility"
  ],
  "state": 2,
  "file_id": 10,
  "knowledge_revision": 51,
  "git_revision": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5",
  "ctags": [],
  "filename": "/home/kavia/workspace/code-maintenance-job-45bd411c/EKYC-2.0/facenet/models/utils/download.py",
  "hash": "cf4b3758f43ca4ad0fe5ffde2164623e",
  "format-version": 4,
  "code-base-name": "https://github.com/DarssiniRamesh/EKYC-2.0.git:main",
  "revision_history": [
    {
      "51": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5"
    }
  ]
}