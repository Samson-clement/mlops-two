import os
import gdown

def download_from_gdrive(drive_link, output_file):
    """
    Downloads a file from Google Drive and saves it with the specified name
    """
    print(f"\nDownloading from {drive_link} to {output_file}")
    
    # Download the file using gdown with the fuzzy option
    gdown.download(drive_link, output_file, quiet=False, fuzzy=True)
    
    # Check if the file was downloaded successfully
    if os.path.exists(output_file):
        print(f"Download complete. File saved as {output_file}")
        
        # Display first few lines of the CSV to verify
        try:
            with open(output_file, 'r') as f:
                first_lines = ''.join([f.readline() for _ in range(3)])
            print(f"\nFirst few lines of {output_file}:")
            print(first_lines)
        except Exception as e:
            print(f"Could not read the file: {e}")
        return True
    else:
        print(f"Download failed for {output_file}.")
        return False

# Files to download
files = [
    {
        "url": "https://drive.google.com/file/d/1k_XlDKnedmbfX8hq-2XkUz__pY7mtqmS/view?usp=sharing",
        "output": "test.csv"
    },
    {
        "url": "https://drive.google.com/file/d/1_lR9J9bzi27mFd4YtG9v-uyYQrsLTQjn/view?usp=sharing",
        "output": "train.csv"
    }
]

# Download all files
successful_downloads = 0
for file_info in files:
    if download_from_gdrive(file_info["url"], file_info["output"]):
        successful_downloads += 1

# Summary
print(f"\nDownload summary: {successful_downloads}/{len(files)} files downloaded successfully.")
