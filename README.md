# image_resizer
A simple Python script to **resize and convert images in batch** using the [Pillow](https://pillow.readthedocs.io/en/stable/) library.

---

## 📌 Features

- Resize all images in a folder to a specific size.
- Convert images to a specified format (e.g., JPEG, PNG).
- Supports common image formats: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`.
- Automatically saves resized images to an output folder.

---

## 🛠️ Requirements

- Python 3.6+
- Pillow (Python Imaging Library)

Install dependencies:

```bash
pip install Pillow
📂 Folder Structure
bash
Copy
Edit
project/
│
├── image_resizer.py        
├── input_images/            # Place your original images here
└── resized_images/          # Output folder (auto-created if not exists)
⚙️ How to Use
Add images to the input_images/ folder.

Configure settings (optional):
Open image_resizer.py and modify:

python
Copy
Edit
output_size = (800, 600)       # Resize to width x height
output_format = "JPEG"         # Desired output format
Run the script:

bash
Copy
Edit
python image_resizer.py
Check the resized_images/ folder for your resized images.

✏️ Example
If you place an image flower.png in input_images/ and run the script, the tool will resize it to 800x600 and save it as flower.jpeg (or other configured format) in resized_images/.

