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
    rotated_image = user_image.rotate(30, expand=True)
    rotated_image.save("tmp_rotated.png")

    user_image.close()
    rotated_image.close()
