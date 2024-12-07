from PIL import Image
from transformers import MobileNetV2ImageProcessor,  MobileNetV2ForImageClassification
import torch
from loadd_model import model
import requests
import io

# Provide the path to your uploaded image
image_path = r"C:\Users\24adi\OneDrive\Desktop\NewFolder\Yoga_Trainer\pp.jpg"

# Open the image
image = Image.open(image_path)

# Load the MobileNetV2 image processor
image_processor = MobileNetV2ImageProcessor.from_pretrained('google/mobilenet_v2_1.0_224')


# Preprocess the image
inputs = image_processor(images=image, return_tensors="pt")

model = MobileNetV2ForImageClassification.from_pretrained(
    "AdityasArsenal/finetuned-for-YogaPoses",
    num_labels=5  # Replace 3 with the number of classes in your dataset
)


# Make predictions with the trained model
model.eval()  # Set the model to evaluation mode
with torch.no_grad():  # Disable gradient calculation
    outputs = model(**inputs)

# Get the predicted class (max logit)
predicted_class = torch.argmax(outputs.logits, dim=-1).item()
names=['Downdog', 'Goddess', 'Plank', 'Tree', 'Warrior2']

# Print the predicted class
print(f"Predicted class index: {predicted_class}:{names[predicted_class]}")

