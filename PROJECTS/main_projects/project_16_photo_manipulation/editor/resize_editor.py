from PIL import Image

class ResizeEditor:
    def __init__(self, image_path: str):
        self.image_path = image_path
        self.image: Image.Image = Image.open(image_path)
        
    def resize(self, width: int, height: int):
        self.image = self.image.resize((width, height))
        
    def save(self, output_path: str):
        self.image.save(output_path)
    