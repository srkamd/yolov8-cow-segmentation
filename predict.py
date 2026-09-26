from ultralytics import YOLO

# Load your trained model
model = YOLO(r"D:\isdi\data\runs\segment\train-2\weights\best.pt")

# Run prediction
results = model.predict(
    source=r"D:\isdi\data\test.jpg",
    save=True,
    conf=0.5
)

print("Prediction complete!")
print("Output saved in the runs/segment folder.")