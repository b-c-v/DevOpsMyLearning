import cv2
import os

# python3 -m venv .tmp
# source .tmp/bin/activate
# pip install opencv-python
image_path = "tmp.png"
try:
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError

except FileNotFoundError:
    print("Image file not found. Please check the path.")

else:
    print(f"Image height: {image.shape[0]} px")
    print(f"Image width: {image.shape[1]} px")
    print(f"Image file size: {os.path.getsize(image_path)/(1024 * 1024):.2f} MB")
