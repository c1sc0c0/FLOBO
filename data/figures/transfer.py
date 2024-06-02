import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image
import numpy as np
import requests
from io import BytesIO

def load_image(image_path, image_size=(256, 256)):
    """Load and preprocess the image."""
    image = Image.open(image_path).convert("RGB")
    image = image.resize(image_size)
    image = np.array(image) / 255.0
    return image

def load_image_from_url(url, image_size=(256, 256)):
    """Load an image from a URL and preprocess it."""
    response = requests.get(url)
    image = Image.open(BytesIO(response.content)).convert("RGB")
    image = image.resize(image_size)
    image = np.array(image) / 255.0
    return image

def save_image(image, output_path):
    """Save the image to the specified file path."""
    image = (image * 255).astype(np.uint8)
    image = Image.fromarray(image)
    image.save(output_path)

def style_transfer(content_image_path, output_image_path, style_image_path):
    """Apply style transfer to an image using a style image URL."""
    # Load the content image
    content_image = load_image(content_image_path, image_size=(256, 256))
    
    # Load the pre-trained model from TensorFlow Hub
    model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

    # Load the style image from the URL
    style_image = load_image(style_image_path, image_size=(256, 256))
    
    # Convert the images to tensors
    content_image_tensor = tf.convert_to_tensor(content_image, dtype=tf.float32)[tf.newaxis, ...]
    style_image_tensor = tf.convert_to_tensor(style_image, dtype=tf.float32)[tf.newaxis, ...]
    
    # Perform style transfer
    stylized_image = model(content_image_tensor, style_image_tensor)[0]
    
    # Save the output image
    save_image(stylized_image.numpy()[0], output_image_path)
    print(f"Styled image saved to {output_image_path}")

if __name__ == "__main__":
    input_image_path = "input.png"
    output_image_path = "output.png"
    style_image_path = "style.png"
    
    style_transfer(input_image_path, output_image_path, style_image_path)
