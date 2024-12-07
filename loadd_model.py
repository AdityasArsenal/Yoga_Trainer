from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import torch
from torchvision import transforms

# Specify the custom directory to save/load the model
custom_dir = r"C:\Users\24adi\OneDrive\Desktop\NewFolder\Yoga_Trainer\model"

# Load model and processor directly from the custom directory
processor = AutoImageProcessor.from_pretrained("AdityasArsenal/finetuned-for-YogaPoses", cache_dir=custom_dir)
model = AutoModelForImageClassification.from_pretrained("AdityasArsenal/finetuned-for-YogaPoses", cache_dir=custom_dir)
