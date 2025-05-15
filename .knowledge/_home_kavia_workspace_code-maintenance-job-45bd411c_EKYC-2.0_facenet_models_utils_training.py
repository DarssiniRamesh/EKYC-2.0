{
  "is_source_file": true,
  "format": "Python",
  "description": "This file contains utility classes and functions for training and evaluating machine learning models, including logging, timing, accuracy calculation, epoch training/evaluation, and data collation functions.",
  "external_files": [
    "torch",
    "numpy",
    "time"
  ],
  "external_methods": [
    "torch.max",
    "torch.tensor",
    "torch.utils.data.DataLoader",
    "torch.optim.Optimizer",
    "torch.optim.lr_scheduler._LRScheduler",
    "torch.utils.tensorboard.SummaryWriter"
  ],
  "published": [
    "accuracy",
    "pass_epoch",
    "collate_pil"
  ],
  "classes": [
    {
      "name": "Logger",
      "description": "A utility class for logging training or validation metrics and losses during model training or evaluation."
    },
    {
      "name": "BatchTimer",
      "description": "A class for tracking the timing of batches during training or evaluation to measure performance."
    }
  ],
  "methods": [
    {
      "name": "accuracy",
      "description": "Calculates the mean accuracy given model logits and true labels."
    },
    {
      "name": "pass_epoch",
      "description": "Handles a training or evaluation epoch, computing loss and metrics over a data loader."
    },
    {
      "name": "collate_pil",
      "description": "Custom collate function for data loaders that process PIL images and labels."
    }
  ],
  "calls": [
    "torch.max",
    "time.time",
    "loss_fn(y_pred, y)",
    "model(x)",
    "optimizer.step()",
    "optimizer.zero_grad()",
    "writer.add_scalars",
    "writer.iteration",
    "writer.add_scalars",
    "writer.add_scalars"
  ],
  "search-terms": [
    "Logger",
    "BatchTimer",
    "pass_epoch",
    "accuracy",
    "collate_pil",
    "training.py",
    "train evaluation",
    "model training utility"
  ],
  "state": 2,
  "file_id": 9,
  "knowledge_revision": 45,
  "git_revision": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5",
  "ctags": [],
  "filename": "/home/kavia/workspace/code-maintenance-job-45bd411c/EKYC-2.0/facenet/models/utils/training.py",
  "hash": "532f3215755188493cd85b796c186521",
  "format-version": 4,
  "code-base-name": "https://github.com/DarssiniRamesh/EKYC-2.0.git:main",
  "revision_history": [
    {
      "45": "2e657f78e47058ae0d9da3cfbc2916dd56d1c4b5"
    }
  ]
}