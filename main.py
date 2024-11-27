#!/usr/bin/env python3
import os
import subprocess

# Activate the virtual environment
venv_path = "venv/bin/activate"
activate_command = f"source {venv_path}"
subprocess.call(activate_command, shell=True, executable='/bin/bash')

# Train the YOLO model
train_command = (
    "yolo detect train "
    "data=datasets/labeled_images/data.yaml "
    "model=yolo11n.pt "
    "epochs=30 "
    "imgsz=640"
)
# subprocess.run(train_command, shell=True)

# Predict using the trained model
predict_command = (
    "yolo predict "
    "source=datasets/test "
    "model=runs/detect/train7/weights/best.pt "
    "data=datasets/labeled_images/data.yaml"
)
subprocess.run(predict_command, shell=True)

# Project path for reference
project_path = "/home/d24680021/Documents/term_project/datasets/labeled_images"
print(f"Project Path: {project_path}")
