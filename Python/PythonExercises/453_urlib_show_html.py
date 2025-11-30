# This code fetches the content of a given URL and prints it to the console using Python's urllib library.

# Import the required module from Python's standard library
import urllib.request  # Provides functions to open and read URLs

# Define the URL we want to open
url = "https://weldering.com"  # Replace this with any URL you want to fetch

try:
    # Open the URL and store the response in a variable
    response = urllib.request.urlopen(url)  # Sends a request to the URL and waits for a response

    # Read the content of the response
    web_content = response.read()  # Reads the HTML/content of the page

    # Decode the bytes to a string (default is UTF-8)
    web_content = web_content.decode('utf-8')  # Converts bytes to readable text

    # Print the content of the page
    print(web_content)  # Display the HTML/content in the console

except urllib.error.URLError as e:
    # Handle errors, like if the URL is invalid or server is down
    print(f"Failed to open URL: {e.reason}")  # Print the reason for failure
