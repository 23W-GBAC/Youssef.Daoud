## [Main Page](README.md) / [1st Automation Post](AutomationNo1.md) / [2nd Automation Post](AutomationPostNo2.md) / 3rd Automation Post / [4th Automation Post](AutomationPostNo4.md) 

# Final Solution, including the potential advantages and disadvantages:

Like I've stated before, I decided on using GitHub Actions to automate a python script that I wrote to check GitHub's logs for the last modification date of all the markdown files in the root directory of my repository. The end result pleased me quite a bit but it left me wanting to do more in regards to how it's shown. For now the script only shows the dates in a terminal or on the GitHub Actions section of the repo which, while good enough for now, can be streamlined further by adding the "Last modified" dates to their respective markdown files automatically. That's something that I've attempted doing before but unfortunately to no avail for reasons I'm not yet aware of. The following is an explanation of how the script works and how GitHub Actions automates the whole process through a simple command.

The process of implementing GitHub Actions for can be broken down into several steps, each and every one of them contributing to a seamless and efficient deployment workflow:

The initial step involves defining a workflow file within the repository's .github/workflows directory. This .yaml file, in my case named check_last_modified.yml, contains instructions for GitHub Actions on how to execute the deployment process. Within this file, the workflow's triggers, jobs, and associated steps are defined. Here's the file:

![image](https://github.com/23W-GBAC/Youssef.Daoud/assets/63427786/ad39cf0a-ec4d-4abd-8f31-0cb8ca990354)



This workflow is triggered by two events:
Scheduled run: It runs every minute according to the cron expression '*/1 * * * *'.
Push event: It runs whenever there is a push to the main branch.

The workflow consists of a single job named check_last_modified, which runs on the latest version of the Ubuntu environment.

This job includes several steps that will be executed sequentially:

Step 1: Checkout repository:
- Uses the actions/checkout@v2 action to clone the repository into the runner's workspace.
Step 2: Set up python:
- Uses the actions/setup-python@v2 action to set up a Python environment. It specifies Python version 3.x.
Step 3: Install the dependencies:
- Installs the required Python packages (requests and pytz) using the pip install command.
Step 4: Run the script:
- Executes the python script located at Automation/automation_2.py. It is run with the specified Python environment and has access to the GitHub token stored in the secrets.GITHUB_TOKEN environment variable. That's the file containing the script.

============================================

Now, as for the python script itself; this Python script interacts with the GitHub API to retrieve the last modified date of the markdown files found in the root directory of my GitHub repository. Here's the code:

![image](https://github.com/23W-GBAC/Youssef.Daoud/assets/63427786/4bb5220c-c583-4d45-8054-f5c476a32dde)

![image](https://github.com/23W-GBAC/Youssef.Daoud/assets/63427786/08f8d181-718a-4d15-a301-81629d276aad)


And here's a breakdown of the code and what it does:

## Imports:

os: Provides a way to interact with the operating system, used for environment variables and file operations.
requests: Allows sending HTTP requests, used for communicating with the GitHub API.
datetime: Provides classes for working with dates and times.
pytz: Handles time zones.
markdown: Used for processing markdown files.

## get_last_modified Function:
Accepts GitHub username, repository name, file_path of the Markdown file, and an optional github_token for authentication.
Sends a request to the GitHub API to get the latest commit information for the specified file.
Extracts the commit date, converts it to UTC, and returns the result.
If an error occurs during the API request, it prints an error message and returns None.

## main Function:
Checks if the script is running in a GitHub Actions environment by checking the presence of the GITHUB_ACTIONS environment variable.
If running in GitHub Actions:
Retrieves GitHub-related environment variables like GITHUB_TOKEN, GITHUB_REPOSITORY_OWNER, and GITHUB_REPOSITORY.
If running locally:
Prompts the user to enter their GitHub username and repository name.
Lists all Markdown files in the current directory.
Iterates through each Markdown file, calling get_last_modified to fetch the last modified date.
Converts the UTC time to the 'Europe/Paris' time zone (UTC+1) and prints the file name along with the last modified date.
Handles cases where the last modified date cannot be retrieved.

## if __name__ == "__main__":
This block ensures that the main function is executed when the script is run directly and not when it's imported as a module.

## Execution:

When the script is run, it uses the GitHub Actions environment. It  lists all Markdown files in the current directory and fetches and prints the last modified date for each file using the GitHub API. The script prints error messages to the console if there are issues with GitHub API requests or if it fails to retrieve the last modified date for a file.

Here's a screenshot of the end result:
![image](https://github.com/23W-GBAC/Youssef.Daoud/assets/63427786/68991de0-dcc7-486c-b651-c558bf4a9762)


## Advantages:
To me, the advantages mostly lie in this solution's simplicity and the fact that it didn't take a long time to get running compared to the other previously-tried methods. There's also enough room for improving the whole thing in different ways to give it more usage in the future for things like being integrated into a continuous integration/continuous deployment (CI/CD) pipeline or visibility notifications and stuff like that.

## Disadvantages:
Of course there are some disadvantages to the whole approach too, it's not really perfect; the GitHub API is subject to rate limiting, so too many script calls will probably result in rate-limiting issues. The whole script relies on the availability and reliability of GitHub's API so if GitHub experiences downtime or if there are changes to the API, the script could stop wokring automatically or something like that. There's also the fact that the script is dependent on GitHub for working so it can't be used elsewhere in an automated way easily without figuring out a whole new way to make it work elsewhere.

There's also the problem that I couldn't get the dates to actually get displayed in the markdown files themselves for some reason, no matter how much I changed the code or GitHub Actions workflow. I assume the lack of error messages meant that it's probably a syntax issue but it got to the point where I couldn't find any solution for this within a short timeframe, so I decided to opt out of implementing it.
