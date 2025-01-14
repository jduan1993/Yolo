from ultralytics import YOLO

# Load a model
model = YOLO("yolo11x.yaml")  # build a new model from YAML
model = YOLO("yolo11x.pt")  # load a pretrained model (recommended for training)
model = YOLO("yolo11x.yaml").load("yolo11x.pt")  # build from YAML and transfer weights

# Train the model
results = model.train(data="datasets/ui.yaml", epochs=100, imgsz=640)