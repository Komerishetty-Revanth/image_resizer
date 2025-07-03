import os
from PIL import Image
input_folder = "input_images"
output_folder = "resized_images"
output_size = (800, 600)
output_format = "JPEG"
def resize_images():
    # Check if input folder exists
    if not os.path.exists(input_folder):
        print(f"❌ Input folder '{input_folder}' does not exist.")
        return
    files = [f for f in os.listdir(input_folder) if f.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif"))]
    if not files:
        print(f"⚠️ No image files found in '{input_folder}'.")
        return
    os.makedirs(output_folder, exist_ok=True)
    for filename in files:
        input_path = os.path.join(input_folder, filename)
        try:
            with Image.open(input_path) as img:
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                img_resized = img.resize(output_size, Image.Resampling.LANCZOS)
                name, _ = os.path.splitext(filename)
                output_filename = f"{name}.{output_format.lower()}"
                output_path = os.path.join(output_folder, output_filename)
                img_resized.save(output_path, output_format)
                print(f"✅ Saved: {output_path}")
        except Exception as e:
            print(f"❌ Error with {filename}: {e}")
if __name__ == "__main__":
    resize_images()
