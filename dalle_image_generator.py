import os
import requests
import base64
from io import BytesIO
from PIL import Image
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class DALLEImageGenerator:
    """
    A class to generate and manipulate images using OpenAI's DALL-E models.
    """
    
    def __init__(self, api_key=None):
        """
        Initialize the OpenAI client with the API key.
        
        Args:
            api_key (str, optional): OpenAI API key. If not provided, will try to get from environment variable.
        """
        # Use provided API key or try to get from environment
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        
        if not self.api_key:
            raise ValueError("OpenAI API key must be provided or set as OPENAI_API_KEY environment variable")
            
        # Initialize the OpenAI client
        self.client = openai.OpenAI(api_key=self.api_key)
    
    def generate_image(self, prompt, size="1024x1024", quality="standard", n=1):
        """
        Generate an image based on the provided prompt using DALL-E.
        
        Args:
            prompt (str): Description of the desired image
            size (str): Size of the generated image (1024x1024, 1792x1024, or 1024x1792)
            quality (str): Quality of the image ('standard' or 'hd')
            n (int): Number of images to generate
            
        Returns:
            list: List of image URLs or None if there was an error
        """
        try:
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size=size,
                quality=quality,
                n=n
            )
            
            # Extract and return the URLs of the generated images
            image_urls = [image.url for image in response.data]
            return image_urls
            
        except Exception as e:
            print(f"Error generating image: {e}")
            return None
    
    def edit_image(self, image_path, mask_path, prompt, size="1024x1024", n=1):
        """
        Edit an existing image using DALL-E.
        
        Args:
            image_path (str): Path to the image to edit
            mask_path (str): Path to the mask image
            prompt (str): Description of the desired edits
            size (str): Size of the output image
            n (int): Number of images to generate
            
        Returns:
            list: List of edited image URLs or None if there was an error
        """
        try:
            # Open and prepare the images
            with open(image_path, "rb") as image_file, open(mask_path, "rb") as mask_file:
                response = self.client.images.edit(
                    image=image_file,
                    mask=mask_file,
                    prompt=prompt,
                    size=size,
                    n=n
                )
            
            # Extract and return the URLs of the edited images
            image_urls = [image.url for image in response.data]
            return image_urls
            
        except Exception as e:
            print(f"Error editing image: {e}")
            return None
    
    def create_image_variation(self, image_path, size="1024x1024", n=1):
        """
        Create variations of an existing image.
        
        Args:
            image_path (str): Path to the image to create variations of
            size (str): Size of the output images
            n (int): Number of variations to generate
            
        Returns:
            list: List of image variation URLs or None if there was an error
        """
        try:
            # Open and prepare the image
            with open(image_path, "rb") as image_file:
                response = self.client.images.create_variation(
                    image=image_file,
                    size=size,
                    n=n
                )
            
            # Extract and return the URLs of the image variations
            image_urls = [image.url for image in response.data]
            return image_urls
            
        except Exception as e:
            print(f"Error creating image variation: {e}")
            return None
    
    @staticmethod
    def download_image(url, save_path=None):
        """
        Download an image from a URL.
        
        Args:
            url (str): URL of the image to download
            save_path (str, optional): Path to save the downloaded image
            
        Returns:
            Image: PIL Image object or None if there was an error
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            
            # Create a PIL Image from the response content
            image = Image.open(BytesIO(response.content))
            
            # Save the image if a save path was provided
            if save_path:
                image.save(save_path)
                print(f"Image saved to {save_path}")
            
            return image
            
        except Exception as e:
            print(f"Error downloading image: {e}")
            return None


def main():
    """
    Example usage of the DALLEImageGenerator class.
    """
    # Check if API key is available
    if not os.getenv("OPENAI_API_KEY"):
        print("Warning: OPENAI_API_KEY not found in environment variables.")
        print("Please provide your API key when creating an instance.")
        return
    
    # Create an instance of the image generator
    generator = DALLEImageGenerator()
    
    # Example prompt for image generation
    prompt = "A futuristic city with flying cars and tall glass buildings at sunset"
    
    # Generate an image
    print(f"Generating image based on prompt: '{prompt}'")
    image_urls = generator.generate_image(prompt)
    
    if image_urls:
        print(f"Generated {len(image_urls)} image(s):")
        for i, url in enumerate(image_urls, 1):
            print(f"{i}. {url}")
        
        # Download the first image
        output_dir = "generated_images"
        os.makedirs(output_dir, exist_ok=True)
        save_path = os.path.join(output_dir, "futuristic_city.png")
        
        image = generator.download_image(image_urls[0], save_path)
        if image:
            # Display image dimensions
            print(f"Image dimensions: {image.width} x {image.height}")


if __name__ == "__main__":
    main()