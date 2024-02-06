# Final Solution, including the potential advantages and disadvantages:

Like I've stated before, I decided on using GitHub Actions to automate a python script that I wrote to check GitHub's logs for the last modification date of all the markdown files in the root directory of my repository. The end result pleased me quite a bit but it left me wanting to do more in regards to how it's shown. For now the script only shows the dates in a terminal or on the GitHub Actions section of the repo which, while good enough for now, can be streamlined further by adding the "Last modified" dates to their respective markdown files automatically. That's something that I've attempted doing before but unfortunately to no avail for reasons I'm not yet aware of. The following is an explanation of how the script works and how GitHub Actions automates the whole process through a simple command.

The process of implementing GitHub Actions for can be broken down into several steps, each and every one of them contributing to a seamless and efficient deployment workflow:

The initial step involves defining a workflow file within the repository's .github/workflows directory. This .yaml file, in my case named check_last_modified.yml, contains instructions for GitHub Actions on how to execute the deployment process. Within this file, the workflow's triggers, jobs, and associated steps are defined. 

The contents of the file are as follows:
name: Check Last Modified

on:
  schedule:
    - cron: '*/1 * * * *'  # Run every 1 minute
  push:
    branches:
      - main

jobs:
  check_last_modified:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.x

      - name: Install dependencies
        run: |
          pip install requests pytz 

      - name: Run script
        run: python Automation/automation_2.py
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

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

Now, as for the python script itself, 

By implementing GitHub Actions for automated deployment, several potential advantages can be realized:

Increased Efficiency: Automation eliminates the need for manual intervention in the deployment process, saving time and reducing the risk of human error. Developers can focus on writing code and implementing features rather than managing deployment tasks.
Consistency and Reliability: Defined workflows ensure that deployments are performed consistently and reliably, following the same steps each time. This consistency enhances the predictability of the deployment process and reduces the likelihood of deployment-related issues.
Scalability: Automated deployment scales seamlessly with the growth of the project, accommodating increased workload and complexity without additional effort. As the project evolves, the deployment workflow can be adapted and expanded to meet new requirements and challenges.
Continuous Integration: Integration with version control enables continuous integration practices, allowing changes to be tested and deployed automatically as they are introduced. This iterative development approach promotes collaboration, feedback, and rapid iteration, leading to faster delivery of new features and improvements.
Community Support: GitHub Actions has a large and active community, with a wide range of pre-built actions and workflows available for common use cases. Developers can leverage existing resources, share knowledge, and collaborate with others to enhance their deployment workflows.

However, it is essential to consider potential disadvantages and limitations of the chosen solution:

Learning Curve: Implementing GitHub Actions may require familiarity with YAML syntax, GitHub workflows, and related concepts, which could pose a learning curve for users new to the platform. Proper documentation, tutorials, and support resources are essential to facilitate the adoption and mastery of GitHub Actions.
Complexity: Depending on the complexity of the deployment process and project requirements, configuring and maintaining the workflow file may require advanced knowledge and troubleshooting skills. Developers must carefully design the workflow to handle edge cases, error conditions, and dependencies effectively.
Dependency on GitHub: GitHub Actions is tightly integrated with the GitHub platform, meaning that reliance on this service could pose a risk if there are service disruptions or changes to the platform's policies. Implementing backup and contingency plans ensures continuity of the deployment process in case of unforeseen issues.
Resource Limitations: GitHub imposes limitations on usage quotas for Actions workflows, including execution time, storage, and concurrent jobs, which could impact larger or resource-intensive projects. Developers must optimize workflows, manage resource usage efficiently, and monitor usage metrics to avoid exceeding quotas and encountering disruptions.

In conclusion, implementing GitHub Actions for automated deployment offers significant advantages in terms of efficiency, reliability, and scalability, making it a compelling solution for streamlining the deployment process of websites and blogs hosted on GitHub Pages. However, careful consideration of potential challenges and limitations is essential to ensure successful implementation and ongoing maintenance of the automated deployment workflow. With proper planning, configuration, and monitoring, GitHub Actions can greatly enhance the development workflow and contribute to the overall success of the project.
