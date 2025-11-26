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
    cv2.imshow("Loaded Image", image)
    cv2.imshow("Blured Image", cv2.blur(image, (50, 50)))

    # Waits for a key press before closing the window.
    # Without this, the window would close immediately.
    cv2.waitKey(0)

    # Destroys all OpenCV windows created by cv2.imshow().
    cv2.destroyAllWindows()
