import os              # Provides functions for interacting with the operating system
import time            # Provides functions for working with time and dates


file_path = input("Enter the full path to the file: ")


# Check whether the file exists before trying to access its metadata
if os.path.exists(file_path):
    # Get the file creation time in seconds since the Unix epoch
    # On Windows: creation time
    # On Unix/Linux: last metadata change time (not true creation time)
    creation_time_seconds = os.path.getctime(file_path)

    # Convert the timestamp into a human-readable date and time
    creation_time_readable = time.ctime(creation_time_seconds)

    # Display the result to the user
    print("File creation date and time:", creation_time_readable)
else:
    # Inform the user if the file path is invalid
    print("The specified file does not exist.")