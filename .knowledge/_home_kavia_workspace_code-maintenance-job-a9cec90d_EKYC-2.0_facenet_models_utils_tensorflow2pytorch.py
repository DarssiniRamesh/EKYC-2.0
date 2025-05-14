{
  "is_source_file": true,
  "format": "Python",
  "description": "This file contains utility functions for converting TensorFlow models to PyTorch, including functions to load model weights, compare outputs, and perform model conversion specifically for models like InceptionResnetV1 and MTCNN components (PNet, RNet, ONet). It appears to be part of a model conversion or utility tool within a facial recognition or face detection project.",
  "external_files": [
    "dependencies.facenet.src",
    "models.inception_resnet_v1",
    "models.mtcnn",
    "facenet",
    "tensorflow"
  ],
  "external_methods": [
    "facenet.load_model",
    "tf.trainable_variables",
    "sess.run",
    "os.path.join",
    "json.dump",
    "tf.reset_default_graph",
    "detect_face.create_mtcnn"
  ],
  "published": [
    "tensorflow2pytorch"
  ],
  "classes": [],
  "methods": [
    {
      "name": "import_tf_params",
      "description": "Imports TensorFlow model parameters from a saved directory, retrieving layer names, parameter arrays, and shapes."
    },
    {
      "name": "get_layer_indices",
      "description": "Maps model layer attribute names to corresponding tensorflow variable indices."
    },
    {
      "name": "load_tf_batchNorm",
      "description": "Loads tensorflow BatchNorm weights into a PyTorch BatchNorm layer."
    },
    {
      "name": "load_tf_conv2d",
      "description": "Loads tensorflow convolution weights into a PyTorch Conv2d layer, with optional transposition."
    },
    {
      "name": "load_tf_conv2d_trans",
      "description": "Loads tensorflow convolution weights into a PyTorch Conv2d layer with transposition."
    },
    {
      "name": "load_tf_basicConv2d",
      "description": "Loads tensorflow weights into a grouped convolution + BatchNorm layer."
    },
    {
      "name": "load_tf_linear",
      "description": "Loads tensorflow weights into a PyTorch Linear layer."
    },
    {
      "name": "load_tf_block35",
      "description": "Loads weights into a specific InceptionResnetV1 block structure."
    },
    {
      "name": "load_tf_block17_8",
      "description": "Loads weights into another InceptionResnetV1 block structure."
    },
    {
      "name": "load_tf_mixed6a",
      "description": "Loads weights into the 'mixed6a' block of the InceptionResnetV1 model."
    },
    {
      "name": "load_tf_mixed7a",
      "description": "Loads weights into the 'mixed7a' block of the InceptionResnetV1 model."
    },
    {
      "name": "load_tf_repeats",
      "description": "Utility function to load repeated blocks of weights into layers."
    },
    {
      "name": "load_tf_repeat_1",
      "description": "Loads repeated block set 1 into a model layer."
    },
    {
      "name": "load_tf_repeat_2",
      "description": "Loads repeated block set 2 into a model layer."
    },
    {
      "name": "load_tf_repeat_3",
      "description": "Loads repeated block set 3 into a model layer."
    },
    {
      "name": "test_loaded_params",
      "description": "Checks if the pytorch model parameters match corresponding tensorflow parameters."
    },
    {
      "name": "compare_model_outputs",
      "description": "Compares the output of the PyTorch and TensorFlow models given test data."
    },
    {
      "name": "compare_mtcnn",
      "description": "Compares outputs between TensorFlow and PyTorch implementations of MTCNN components."
    },
    {
      "name": "load_tf_model_weights",
      "description": "Main function that loads tensorflow weights into a PyTorch model given a layer lookup dictionary."
    },
    {
      "name": "tensorflow2pytorch",
      "description": "Main orchestrator function that defines layer mappings for various models (InceptionResnet, PNet, RNet, ONet) and performs loading and conversion, including saving model states and weights."
    }
  ],
  "calls": [
    "facenet.load_model",
    "tf.trainable_variables",
    "sess.run",
    "json.dump",
    "os.path.join",
    "tf.reset_default_graph",
    "detect_face.create_mtcnn",
    "torch.save",
    "torch.tensor"
  ],
  "search-terms": [
    "tensorflow2pytorch",
    "load_tf_model_weights",
    "InceptionResnetV1",
    "facenet",
    "mtcnn",
    "convert",
    "weights",
    "model conversion"
  ],
  "state": 2,
  "file_id": 8,
  "knowledge_revision": 53,
  "git_revision": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5",
  "ctags": [],
  "filename": "/home/kavia/workspace/code-maintenance-job-a9cec90d/EKYC-2.0/facenet/models/utils/tensorflow2pytorch.py",
  "hash": "2f634a1ceaa93d21f5598cde55fb4e11",
  "format-version": 4,
  "code-base-name": "https://github.com/DarssiniRamesh/EKYC-2.0.git:main",
  "revision_history": [
    {
      "53": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5"
    }
  ]
}