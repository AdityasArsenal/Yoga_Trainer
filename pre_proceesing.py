from PIL import Image
import torch
from torchvision import transforms

# Define preprocessing transformations (resize + normalize)
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),  # MobileNetV2 standard values
])

# Load and preprocess the image
image = Image.open("your_image_path.jpg")
image = transform(image).unsqueeze(0)  # Add batch dimension

# Load the model
model = torch.load("path_to_model.safetensors", map_location=torch.device('cpu'))

# Inference
model.eval()
with torch.no_grad():
    outputs = model(image)
