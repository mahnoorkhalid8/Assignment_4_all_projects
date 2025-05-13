from PIL import ImageDraw, ImageFont
from PIL import Image

class WatermarkEditor:
    def __init__(self, image_path: str):
        self.image: Image.Image = Image.open(image_path)
        
    def add_watermark(self, text: str, position=(10, 10)):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.load_default()
        draw.text(position, text, fill=(255, 255, 255), font=font)
        
    def save(self, output_path: str):
        self.image.save(output_path)
        