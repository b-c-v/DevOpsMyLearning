from PIL import Image, ImageDraw, ImageFont

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

    # Create a drawing object that allows us to draw on the image
    draw = ImageDraw.Draw(user_image)

    text = "I love Python!"
    text_position = (250, 250)
    text_color = (255, 24, 54)
    text_size = 50

    font = ImageFont.truetype("arial.ttf", text_size)

    # Draw the text onto the image
    draw.text(text_position, text, fill=text_color, font=font)

    user_image.show()

    # Save the updated image to a new file
    user_image.save("tmp_with_text.png")

    user_image.close()

# -----------------------------
# JOIN TWO IMAGES
# -----------------------------

# Open two images to be joined
image1 = Image.open("tmp.png")
image2 = Image.open("tmp_with_text.png")

# Ensure both images are in the same mode (e.g., RGB)
image1 = image1.convert("RGB")
image2 = image2.convert("RGB")

# Get dimensions of the images
width1, height1 = image1.size
width2, height2 = image2.size


# ---- JOIN HORIZONTALLY ----

# Create a new blank image with combined width and max height
horizontal_image = Image.new(
    "RGB",
    (width1 + width2, max(height1, height2)),
    color=(0, 0, 0),  # Background text_color (black)
)

# Paste the first image on the left
horizontal_image.paste(image1, (0, 0))

# Paste the second image to the right of the first image
horizontal_image.paste(image2, (width1, 0))

# Save the horizontally joined image
horizontal_image.save("tmp_joined.png")

horizontal_image.show()

horizontal_image.close()
