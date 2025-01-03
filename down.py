import requests
import pandas as pd
import os

def download_file(url, download_folder):
    # Get the file name from the URL
    file_name = url.split('/')[-1]
    file_path = os.path.join(download_folder, file_name)

    # Send a GET request to the file URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Open the file in write-binary mode and save the content
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {file_name} to {file_path}")
    else:
        print(f"Failed to download {file_name}. Status code: {response.status_code}")

# Example usage
github_url = "https://raw.githubusercontent.com/username/repository/branch/filename.ext"
save_to = "local_filename.ext"
df=pd.read_excel("Book1.xlsx")
for l in df.url:
    download_file(l, "C:/Users/pulag/Desktop/git/assignment/icons")
