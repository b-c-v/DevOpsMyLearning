import cv2

# Load the video file
video_path = "tmp.mp4"
cap = cv2.VideoCapture(video_path)  # Open the video file for reading

# Check if the video was opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")  # Print an error message if file can't be opened
    exit()  # Exit the program

# Loop through the frames of the video
while True:
    ret, frame = cap.read()  # Read the next frame from the video
    if not ret:  # If no frame is returned, the video has ended
        break  # Exit the loop

    # Display the frame in a window
    cv2.imshow("Video", frame)  # "Video" is the window name

    # Wait for 25ms and check if the user pressed 'q' to quit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break  # Exit the loop if 'q' is pressed

# Release the video capture object and close all windows
cap.release()  # Release the video file
cv2.destroyAllWindows()  # Close the display window