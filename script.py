from github import Github
from dotenv import load_dotenv
import os
from git import Repo
import subprocess
 
# Load environment variables from .env file
load_dotenv()

GIT_TOKEN = os.getenv("GIT_TOKEN")
BRANCH = os.getenv("BRANCH")

# print(GIT_TOKEN)
# Auth the Repo
github_access = Github(GIT_TOKEN)

user = github_access.get_user()
print("Authenticated as:", user.login)

# Get Repo Access
repo = github_access.get_repo("thirumalai-py/ci-cd-html")

# repo_path = "thirumalai-py/ci-cd-html"  # Replace with your local repo path
repo_path = os.getcwd()
repo_src = Repo(repo_path)


# Get repository details
print(repo.full_name)
print(repo.description)

branch_name = "dev"
# Get commits
commits = repo.get_commits(sha=branch_name)

# Get Total count
# print(commits.totalCount)
# for commit in commits:
#     print(commit.sha)

# print("Latest commit: ", commits[0])

latest_commit = commits[0]
recent_commit = latest_commit.sha
print(recent_commit)


commit_file = 'latest_commit.txt'

# # Pull latest changes from the remote repository
# origin = repo_src.remotes.origin
# origin.pull()

# print("Git pull completed successfully!")

if os.path.exists(commit_file):
    with open(commit_file, 'r') as file:
        last_commit = file.readline().strip()
        print("Last commit: ", last_commit)
    if recent_commit==last_commit:
        print("No new commits found")
    else:
        # Pull latest changes from the remote repository
        origin = repo_src.remotes.origin
        origin.pull()

        print("Git pull completed successfully!")
        # Save the last commit
        with open(commit_file, 'w') as file:
            file.write(recent_commit)
else:
    # Save the last commit
    with open(commit_file, 'w') as file:
        file.write(recent_commit)




