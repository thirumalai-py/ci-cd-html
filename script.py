from github import *

GIT_TOKEN = "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"

# Auth the Repot

# using an access token
auth = Auth.Token(GIT_TOKEN)

github_access = Github(GIT_TOKEN)

# Get Repo Access
repo = github_access.get_repo("thirumalai-py/ci-cd-html")

# Get repository details
print(repo.full_name)
print(repo.description)
