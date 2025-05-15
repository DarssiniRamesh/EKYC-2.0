{
  "is_source_file": true,
  "format": "Python",
  "description": "This file defines the InceptionResnetV1 model architecture used for face recognition, including multiple convolutional blocks, mixed modules, and the main model class with optional pretrained weights loading.",
  "external_files": [
    "./utils/download"
  ],
  "external_methods": [
    "download_url_to_file"
  ],
  "published": [
    "InceptionResnetV1",
    "load_weights",
    "get_torch_home"
  ],
  "classes": [
    {
      "name": "BasicConv2d",
      "description": "A convolutional module with batch normalization and ReLU activation used as a building block."
    },
    {
      "name": "Block35",
      "description": "A residual block with multiple convolutional branches, part of the Inception-ResNet architecture."
    },
    {
      "name": "Block17",
      "description": "A residual block with a different convolutional branch architecture, used within the network."
    },
    {
      "name": "Block8",
      "description": "Another residual block with options to include or exclude the ReLU activation."
    },
    {
      "name": "Mixed_6a",
      "description": "A module performing mixed operations including convolutions and pooling, used to reduce spatial dimensions."
    },
    {
      "name": "Mixed_7a",
      "description": "A mixed module similar to Mixed_6a but with different configurations and more branches."
    },
    {
      "name": "InceptionResnetV1",
      "description": "Main class implementing the Face Recognition network with optional pretrained weights and classification capabilities."
    }
  ],
  "methods": [
    {
      "name": "forward",
      "description": "Defines the forward pass of the InceptionResnetV1 model, outputting either face embeddings or logits."
    },
    {
      "name": "load_weights",
      "description": "Downloads and loads pretrained weights into the model based on dataset name."
    },
    {
      "name": "get_torch_home",
      "description": "Returns the directory path used for storing Torch related files, including pretrained weights."
    }
  ],
  "calls": [
    "download_url_to_file",
    "torch.load",
    "os.makedirs",
    "os.path.join",
    "os.path.exists",
    "get_torch_home"
  ],
  "search-terms": [
    "InceptionResnetV1",
    "facenet",
    "face recognition",
    "residual blocks",
    "Mixed Modules",
    "pretrained weights",
    "face embeddings"
  ],
  "state": 2,
  "file_id": 6,
  "knowledge_revision": 41,
  "git_revision": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5",
  "ctags": [],
  "filename": "/home/kavia/workspace/code-maintenance-job-45bd411c/EKYC-2.0/facenet/models/inception_resnet_v1.py",
  "hash": "1e997f7b21614b29ab2794aedc310222",
  "format-version": 4,
  "code-base-name": "https://github.com/DarssiniRamesh/EKYC-2.0.git:main",
  "revision_history": [
    {
      "41": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5"
    }
  ]
}