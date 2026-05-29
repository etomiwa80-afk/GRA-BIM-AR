from ultralytics import YOLO

# Load segmentation model
model = YOLO("yolo11n-seg.pt")

print("Running YOLO segmentation on your room...\n")

# Run on your actual room photo
results = model("room.jpg")

# Print everything detected
print("Objects detected in your room:")
for r in results:
    for c in r.boxes.cls:
        print(f"  - {model.names[int(c)]}")

# Save annotated image
results[0].save("seg_room.jpg")
print("\nSaved result as seg_room.jpg")
print("Open that file to see the segmentation masks!") 
