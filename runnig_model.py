from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import torch
from loadd_model import model, processor

# Load and preprocess the image
image = Image.open("yogap.jpg")
inputs = processor(images=image, return_tensors="pt")

# Make predictions
with torch.no_grad():
    outputs = model(**inputs)

# Get the predicted class
logits = outputs.logits
predicted_class_idx = torch.argmax(logits, dim=-1).item()
print(f"Predicted class index: {predicted_class_idx}")
