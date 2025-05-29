from PIL import Image

class PhotoEditor:
    def __init__(self, image_path: str):
        self.image = Image.open(image_path)
        
    def save(self, output_path: str):
        self.image.save(output_path)