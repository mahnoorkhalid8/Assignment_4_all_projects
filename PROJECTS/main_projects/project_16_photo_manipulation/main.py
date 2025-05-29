from editor.resize_editor import ResizeEditor
from editor.filter_editor import FilterEditor
from editor.watermark_editor import WatermarkEditor

# choose an image
image_path = "images/photo1.jpg"
output_path = "output/edited.jpg"

# Apply operations
editor = ResizeEditor(image_path)
editor.resize(300, 300)

# Enhance filter
filter_editor = FilterEditor(image_path)
filter_editor.enhance_color(1.5)
filter_editor.enhance_brightness(1.2)

# Add watermark
watermark_editor = WatermarkEditor(image_path)
watermark_editor.add_watermark("Mahnoor")

# save final image
watermark_editor.save(output_path)
print(f"Saved at: {output_path}")