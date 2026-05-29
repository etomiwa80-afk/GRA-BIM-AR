from ultralytics import YOLO

# Download and load pretrained model
model = YOLO("yolo11n.pt")

# Run on a sample image
results = model.predict("https://ultralytics.com/images/bus.jpg", save=True)

print("Detection complete! Check the runs folder for results.")
