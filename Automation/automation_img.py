import requests
from github import Github
from io import BytesIO
from PIL import Image

# GitHub credentials
github_token = "YOUR_GITHUB_TOKEN"  # Replace with your GitHub token
repo_owner = "YOUR_USERNAME"  # Replace with your GitHub username
repo_name = "YOUR_REPO_NAME"  # Replace with your repository name

# Website URL from which to fetch images
website_url = "https://example.com"  # Replace with the target website URL

def fetch_and_upload_images():
    # Authenticate with GitHub using your token
    g = Github(github_token)
    repo = g.get_user(repo_owner).get_repo(repo_name)

    # Fetch images from the website
    response = requests.get(website_url)
    if response.status_code == 200:
        html_content = response.text

        # Extract image URLs from the HTML content (you may need to use a more advanced HTML parser)
        image_urls = extract_image_urls(html_content)

        # Upload each image to the GitHub repository
        for img_url in image_urls:
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                img_data = BytesIO(img_response.content)
                img = Image.open(img_data)

                # Save the image to a temporary file
                img_path = "/path/to/temp/image.jpg"  # Replace with an appropriate path
                img.save(img_path)

                # Upload the image to the GitHub repository
                upload_image_to_github(repo, img_path)

def extract_image_urls(html_content):
    # Implement your own logic to extract image URLs from the HTML content
    # You may use a library like BeautifulSoup for more advanced HTML parsing
    # For simplicity, let's assume all image URLs end with ".jpg"
    return [url for url in html_content.split() if url.endswith(".jpg")]

def upload_image_to_github(repo, img_path):
    # Upload the image to the GitHub repository
    with open(img_path, "rb") as img_file:
        content = img_file.read()
        img_name = img_path.split("/")[-1]  # Extract the image name from the path
        img_path_in_repo = f"images/{img_name}"  # Specify the path where you want to store images in the repo

        # Create or update the image file in the GitHub repository
        try:
            repo.create_file(img_path_in_repo, f"Add image: {img_name}", content, branch="main")
            print(f"Image '{img_name}' uploaded successfully.")
        except Exception as e:
            print(f"Error uploading image '{img_name}': {e}")

if __name__ == "__main__":
    fetch_and_upload_images()
