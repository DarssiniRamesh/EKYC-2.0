{
  "is_source_file": true,
  "format": "Python",
  "description": "This file defines the VGGFace neural network model and a helper function to load it with pretrained weights. It includes class definition for VGGFace, a method to get the device, a forward pass implementation, and a load_model function to initialize and load weights.",
  "external_files": [
    "weights/vggface_weights.pt"
  ],
  "external_methods": [
    "torch.load",
    "os.path.join",
    "os.path.dirname",
    "torch.cuda.is_available"
  ],
  "published": [
    "VGGFace",
    "load_model"
  ],
  "classes": [
    {
      "name": "VGGFace",
      "description": "A PyTorch neural network module implementing the VGGFace architecture for face recognition."
    }
  ],
  "methods": [
    {
      "name": "device",
      "description": "Returns the device (CPU or GPU) on which the model parameters are located."
    },
    {
      "name": "forward",
      "description": "Defines the forward pass of the network, applying convolutional, activation, pooling, fully connected, dropout, and softmax layers."
    },
    {
      "name": "load_model",
      "description": "Loads the VGGFace model with optional pretrained weights, setting the device appropriately."
    }
  ],
  "calls": [
    "next(self.parameters())",
    "super().__init__()",
    "F.relu",
    "F.max_pool2d",
    "x.view",
    "F.dropout",
    "F.softmax",
    "torch.load",
    "os.path.join",
    "os.path.dirname",
    "torch.device",
    "torch.cuda.is_available"
  ],
  "search-terms": [
    "VGGFace architecture",
    "face recognition model",
    "load pretrained weights",
    "PyTorch neural network",
    "VGGFace class",
    "load_model function"
  ],
  "state": 2,
  "file_id": 15,
  "knowledge_revision": 48,
  "git_revision": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5",
  "ctags": [],
  "filename": "/home/kavia/workspace/code-maintenance-job-45bd411c/EKYC-2.0/verification_models/VGGFace.py",
  "hash": "4afd68578e6aa48245232c5d0b2ab097",
  "format-version": 4,
  "code-base-name": "https://github.com/DarssiniRamesh/EKYC-2.0.git:main",
  "revision_history": [
    {
      "48": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5"
    }
  ]
}