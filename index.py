from ultralytics import YOLO

def main():
    # Segmentation ke liye yolov8n-seg.pt (kyun ke annotations polygon masks hain)
    # Agar sirf bounding box detection chahiye to "yolov8n.pt" use kar sakte hain
    model = YOLO("yolov8n-seg.pt")

    results = model.train(
        data="data.yaml",
        epochs=10,
        imgsz=640,
        batch=8,
        device="cpu"
    )

if __name__ == "__main__":
    main()