# 🐄 Cow Instance Segmentation Dataset (YOLOv8)

## 📌 Subtitle (For Kaggle Subtitle field)
> Custom polygon-annotated cattle dataset for instance segmentation with YOLOv8 (99% mAP50).

---

## 📖 Context
Automated livestock monitoring, health inspection, and body weight/condition scoring require precise animal localization and boundary extraction. This dataset was curated and annotated with high-precision polygon masks to train and evaluate computer vision models for cattle instance segmentation in agricultural environments.

---

## 📁 Content & Structure
The dataset follows standard **YOLOv8 Segmentation format** ready for training out of the box:

```text
cow-segmentation-dataset/
├── images/
│   └── train/      # 98 High-resolution cattle images (.jpg)
├── labels/
│   └── train/      # 97 YOLO polygon mask annotation files (.txt)
└── data.yaml       # Dataset configuration file for Ultralytics YOLO
```

### Classes:
- **`0`**: `cow` (Cattle)

---

## 🏷️ Annotation Format
Annotations are provided as normalized polygon segmentation coordinates:
```text
<class-id> <x1> <y1> <x2> <y2> ... <xn> <yn>
```
Where each coordinate pair represents the exact contour boundary of the animal.

---

## 🚀 Benchmark Model Performance
Trained on YOLOv8 nano segmentation (`yolov8n-seg`) over 10 epochs:
- **Precision:** `98.7%` (Bounding Box), `97.8%` (Mask)
- **Recall:** `96.4%` (Bounding Box), `95.5%` (Mask)
- **mAP50:** `99.0%` (Bounding Box), `97.2%` (Mask)

---

## 💡 Inspiration & Use Cases
- Precision Agriculture & Smart Livestock Farming
- Cattle posture and body condition analysis
- Automated count and boundary masking in cattle sheds
- Comparative benchmark between object detection and instance segmentation

---

## 🔗 Code & Pre-trained Weights
The complete training pipeline, trained weights (`best.pt`), and inference code are available on GitHub:
👉 [GitHub: srkamd/yolov8-cow-segmentation](https://github.com/srkamd/yolov8-cow-segmentation)
