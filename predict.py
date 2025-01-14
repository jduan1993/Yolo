from ultralytics import YOLO

# Load a pretrained YOLO11n model
model = YOLO("./runs/detect/train/weights/best.pt")

# Define path to the image file
source = "./labelimg/merge_image/merged_image.jpg"

# Run inference on the source
model.predict(source, save=True, save_frames=True, save_txt=True, save_conf=True, save_crop=True, imgsz=640, conf=0.8)