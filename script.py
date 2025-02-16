from github import *
from dotenv import load_dotenv
import os
 
# Load environment variables from .env file
load_dotenv()

GIT_TOKEN = os.getenv("GIT_TOKEN")

# print(GIT_TOKEN)
# Auth the Repo
github_access = Github(GIT_TOKEN)

user = github_access.get_user()
print("Authenticated as:", user.login)

# Get Repo Access
repo = github_access.get_repo("thirumalai-py/ci-cd-html")

# Get repository details
print(repo.full_name)
print(repo.description)

# Get commits
commits = repo.get_commits()

# Get Total count
# print(commits.totalCount)

# print("Latest commit: ", commits[0])

latest_commit = commits[0]

print(latest_commit.sha)
