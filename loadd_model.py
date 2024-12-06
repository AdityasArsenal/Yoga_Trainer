# Load model directly
from transformers import AutoImageProcessor, AutoModelForImageClassification

processor = AutoImageProcessor.from_pretrained("AdityasArsenal/finetuned-for-YogaPoses")
model = AutoModelForImageClassification.from_pretrained("AdityasArsenal/finetuned-for-YogaPoses")

print(type(model))