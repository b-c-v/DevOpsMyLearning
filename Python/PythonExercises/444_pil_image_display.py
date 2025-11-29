from PIL import Image

# python3 -m venv .tmp
# source .tmp/bin/activate
# pip install pillow
image_path = "tmp.png"

try:
    # Open an image file from the given path
    user_image = Image.open(image_path)
    if user_image is None:
        raise FileNotFoundError

except FileNotFoundError:
    print("Image file not found. Please check the path.")

else:
    user_image.show()

    user_image.close()
