import os
import random
import numpy as np
from PIL import Image, ImageOps

def apply_random_noise(image):
    """Apply random noise to an image."""
    # Convert image to numpy array
    img_array = np.array(image)
    
    # Generate random noise
    noise = np.random.normal(0, 25, img_array.shape)  # mean=0, std=25 (you can adjust this)
    
    # Add the noise to the image
    noisy_img = img_array + noise
    
    # Clip the values to stay within valid pixel range [0, 255]
    noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)
    
    # Convert back to PIL image
    return Image.fromarray(noisy_img)

def apply_random_flip(image):
    """Randomly flip the image horizontally or vertically."""
    if (True):
        return image.transpose(Image.FLIP_LEFT_RIGHT)  # Flip horizontally

def augment_images_in_folder(folder_path):
    """Loop through each image in the folder, apply random transformations, and save the result."""
    # Ensure the folder exists
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} does not exist!")
        return
    
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Skip if not an image file (you can add more file types if needed)
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue
        
        # Open the image
        image = Image.open(file_path)
        
        # Decide randomly whether to apply noise or flip
        if random.choice([True, False]):
            # Apply random noise
            augmented_image = apply_random_noise(image)
            new_filename = f"noisy_{filename}"
        else:
            # Apply random flip
            augmented_image = apply_random_flip(image)
            new_filename = f"flipped_{filename}"
        
        # Save the augmented image back in the same folder
        augmented_image.save(os.path.join(folder_path, new_filename))
        print(f"Saved augmented image: {new_filename}")

# Example usage
folder_path = r"C:\Users\24adi\.cache\kagglehub\datasets\niharika41298\yoga-poses-dataset\DATASET"  # Replace with your folder path
augment_images_in_folder(folder_path)

