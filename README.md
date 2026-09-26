# YOLOv8 Cow Instance Segmentation

This project trains a custom YOLOv8 segmentation model (`yolov8n-seg`) to detect and segment cows from images.

## Results
- **Precision:** 98.7% (Box), 97.8% (Mask)
- **Recall:** 96.4% (Box), 95.5% (Mask)
- **mAP50:** 99.0% (Box), 97.2% (Mask)

## Project Structure
```text
├── images/
│   └── train/              # Dataset images
├── labels/
│   └── train/              # YOLO polygon segmentation annotations
├── runs/
│   └── segment/train-2/    # Training results, graphs, and weights
│       └── weights/best.pt # Trained model weights
├── data.yaml               # YOLO dataset configuration
├── index.py                # Training script
└── README.md
```

## Getting Started

### 1. Requirements
Install the required packages:
```bash
pip install ultralytics opencv-python
```

### 2. Train the Model
```bash
python index.py
```

### 3. Inference / Prediction
```python
from ultralytics import YOLO

model = YOLO("runs/segment/train-2/weights/best.pt")
results = model.predict(source="images/train", save=True, show=True)
```
