import os
from PIL import Image
input_folder = "ai.jpg"        
output_folder = "resized_images"    
output_size = (800, 600)             
output_format = "JPEG"             

def resize_images():
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
            input_path = os.path.join(input_folder, filename)
            try:
                with Image.open(input_path) as img:
                    img_resized = img.resize(output_size, Image.ANTIALIAS)
                    name, _ = os.path.splitext(filename)
                    output_filename = f"{name}.{output_format.lower()}"
                    output_path = os.path.join(output_folder, output_filename)
                    img_resized.save(output_path, output_format)
                    print(f"Saved: {output_path}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")
if __name__ == "__main__":
    resize_images()
