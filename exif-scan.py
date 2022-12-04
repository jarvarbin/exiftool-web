import requests
from exiftool import ExifTool

# Set the base URL of the website
base_url = "https://www.example.com"

# Set the URL path to search for files
path = "/files"

# Set the file extensions to search for
extensions = ["jpg", "png", "mp4"]

# Set the name of the CSV file to save the results
csv_file = "metadata.csv"

# Set the headers for the HTTP request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}

# Create an instance of the ExifTool class
exiftool = ExifTool()

# Set up the HTTP session
session = requests.Session()

# Set the URL of the page to search for files
url = base_url + path

# Send a GET request to the URL
response = session.get(url, headers=headers)

# Check if the response is successful
if response.status_code == 200:
    # Parse the HTML content of the page
    html = response.text

    # Find all links on the page
    links = re.findall(r'<a href="([^"]+)">', html)

    # Set the headers for the CSV file
    csv_headers = ["Filename", "File Size", "File Type", "Image Width", "Image Height"]

    # Open the CSV file in write mode
    with open(csv_file, "w") as f:
        # Create a CSV writer
        writer = csv.writer(f)

        # Write the headers to the CSV file
        writer.writerow(csv_headers)

        # Iterate over the links on the page
        for link in links:
            # Get the filename and extension from the link
            filename, file_ext = os.path.splitext(link)
