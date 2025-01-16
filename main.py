# Import required libraries
from keras.models import load_model  # For loading the trained TensorFlow model
from PIL import Image, ImageOps  # For image processing (install pillow library)
import numpy as np  # For numerical computations
import matplotlib.pyplot as plt  # For displaying the input image

# Disable scientific notation for better clarity in output
np.set_printoptions(suppress=True)

# Load the trained model (update the path to match your setup)
model = load_model("/content/keras_model.h5", compile=False)

# Load the class labels from the text file
with open("/content/labels.txt", "r") as file:
    class_names = file.readlines()

# Function to predict the class of an input image
def predict_image(image_path):
    """
    This function accepts an image path, preprocesses the image, 
    and predicts its class using the trained model.
    
    Args:
        image_path (str): Path to the image to be predicted.
    """
    try:
        # Open the image and convert it to RGB format
        image = Image.open(image_path).convert("RGB")
        
        # Resize and crop the image to the required size (224x224)
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
        
        # Display the input image
        plt.imshow(image)
        plt.axis("off")  # Hide axes for cleaner display
        plt.title(f"Input Image: {image_path}")
        plt.show()
        
        # Convert the image to a numpy array
        image_array = np.asarray(image)
        
        # Normalize the pixel values to the range [-1, 1]
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
        
        # Prepare the image array for model input
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        data[0] = normalized_image_array
        
        # Predict the class using the loaded model
        prediction = model.predict(data)
        
        # Determine the class with the highest prediction score
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]
        
        # Print the predicted class and its confidence score
        print(f"Image: {image_path}")
        print("Class:", class_name.strip())  # Strip to remove trailing newline
        print("Confidence Score:", confidence_score)
        print("-" * 50)
    
    except Exception as e:
        # Handle exceptions and provide an error message
        print(f"Error processing image {image_path}: {e}")
        print("-" * 50)

# List of image paths to process
image_paths = [
    "/content/test.jpg",
    "/content/test2.jpg",
    "/content/test3.png"
]

# Predict the class for each image in the list
for image_path in image_paths:
    print(f"Testing image: {image_path}")
    predict_image(image_path)
