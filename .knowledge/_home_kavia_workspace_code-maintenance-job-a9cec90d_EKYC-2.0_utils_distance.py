{
  "is_source_file": true,
  "format": "Python",
  "description": "This file defines functions for computing various distance metrics (L1, Euclidean, Cosine) between tensor vectors, along with a utility to find threshold values for different models and metrics. It includes some test cases in the main block.",
  "external_files": [
    "numpy",
    "torch"
  ],
  "external_methods": [
    "np"
  ],
  "torch.abs, torch.mean, torch.sum, torch.sqrt, torch.square, torch.dot, torch.norm, torch.math.acos, torch.rand": "",
  "published": [],
  "classes": [],
  "methods": [
    {
      "name": "L1_Distance",
      "description": "Calculates the L1 distance (Manhattan distance) between two tensors with optional reduction ('sum' or 'mean')."
    },
    {
      "name": "Euclidean_Distance",
      "description": "Calculates the Euclidean distance between two tensors."
    },
    {
      "name": "Cosine_Distance",
      "description": "Calculates the cosine distance between two tensors."
    },
    {
      "name": "findThreshold",
      "description": "Returns a threshold value based on the model name and distance metric, with predefined defaults and model-specific overrides."
    }
  ],
  "calls": [
    "torch.abs",
    "torch.mean",
    "torch.sum",
    "torch.sqrt",
    "torch.square",
    "torch.dot",
    "torch.norm",
    "torch.math.acos",
    "torch.rand"
  ],
  "search-terms": [
    "distance metrics",
    "cosine distance",
    "Euclidean distance",
    "L1 distance",
    "threshold finder",
    "face recognition",
    "torch tensors"
  ],
  "state": 2,
  "file_id": 18,
  "knowledge_revision": 54,
  "git_revision": "d1e36568fc828d61f29ebe58995c7a10be68814c",
  "ctags": [],
  "filename": "/home/kavia/workspace/code-maintenance-job-a9cec90d/EKYC-2.0/utils/distance.py",
  "hash": "5aab522a11f0c0771e1acb09548f553a",
  "format-version": 4,
  "code-base-name": "https://github.com/DarssiniRamesh/EKYC-2.0.git:main",
  "revision_history": [
    {
      "54": "d1e36568fc828d61f29ebe58995c7a10be68814c"
    }
  ]
}