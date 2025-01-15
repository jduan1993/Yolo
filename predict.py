from ultralytics import YOLO

# Load a pretrained YOLO11n model
model = YOLO("./runs/detect/train2/weights/best.pt")

# Define path to the image file
source = "./pre_data/global_color1/global_color1.jpg"

# Run inference on the source
model.predict(source, save=True, save_frames=True, save_txt=True, save_conf=True, save_crop=True, imgsz=640)