from tensorflow.keras.models import load_model

# Load the model with custom_objects to handle any unknown layers
model = load_model('lala.h5')
