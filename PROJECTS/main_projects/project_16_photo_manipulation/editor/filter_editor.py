from PIL import ImageEnhance
from PIL import Image

class FilterEditor:
    def __init__(self, image_path: str):
        self.image: Image.Image = Image.open(image_path)
        
    def enhance_color(self, factor: float):
        enhancer = ImageEnhance.Color(self.image)
        self.image = enhancer.enhance(factor)
        
    def enhance_brightness(self, factor: float):
        enhancer = ImageEnhance.Brightness(self.image)
        self.image = enhancer.enhance(factor)
        
    def save(self, output_path: str):
        self.image.save(output_path)