import cv2

# python3 -m venv .tmp
# source .tmp/bin/activate
# pip install opencv-python

try:
    image = cv2.imread("tmp.png")
    if image is None:
        raise FileNotFoundError
except FileNotFoundError:
    print("Image file not found. Please check the path.")

cv2.imshow("Loaded Image", image)

# Waits for a key press before closing the window.
# Without this, the window would close immediately.
cv2.waitKey(0)

# Destroys all OpenCV windows created by cv2.imshow().
cv2.destroyAllWindows()