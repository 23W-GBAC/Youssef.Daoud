import os
import requests
from datetime import datetime
import sys

def get_last_modified(username, repository, file_path, github_token=None):
    try:
        headers = {}
        
        if github_token:
            headers['Authorization'] = f'Bearer {github_token}'

        # Fetch the last commit information for the file using GitHub API
        api_url = f'https://api.github.com/repos/{username}/{repository}/commits?path={file_path}&per_page=1'
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            last_commit_data = response.json()[0]
            last_commit_date_str = last_commit_data['commit']['committer']['date']
            last_commit_date = datetime.strptime(last_commit_date_str, '%Y-%m-%dT%H:%M:%SZ')
            return last_commit_date
        else:
            print(f"GitHub API error: {response.status_code} - {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def main():
    if 'GITHUB_ACTIONS' in os.environ:
        # Running in GitHub Actions environment
        github_token = os.getenv('GITHUB_TOKEN')
        username = os.getenv('GITHUB_REPOSITORY_OWNER')
        repository = os.getenv('GITHUB_REPOSITORY').split('/')[1]
    else:
        # Running locally, prompt for user input
        username = input("Enter your GitHub username: ")
        repository = input("Enter the GitHub repository name: ")
        github_token = None

    # Set the directory containing Markdown files
    markdown_files_dir = 'path/to/your/markdown/files'

    # List all Markdown files in the directory
    markdown_files = [file for file in os.listdir(markdown_files_dir) if file.endswith('.md')]

    # Iterate through each Markdown file and get the last modified date
    for file_name in markdown_files:
        file_path = os.path.join(markdown_files_dir, file_name)
        last_modified_date = get_last_modified(username, repository, file_path, github_token)

        if last_modified_date:
            print(f"File: {file_name}, Last modified on: {last_modified_date}")
        else:
            print(f"Unable to retrieve last modification date for file: {file_name}")

if __name__ == "__main__":
    main()