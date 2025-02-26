# GitHub Auto-Pull Script

This Python script simplifies keeping a local GitHub repository in sync with a remote branch. It automatically checks for and pulls new commits.

## What it Does

The script authenticates with GitHub, checks for new commits on a specified branch, and pulls the latest changes if any are found.  It uses a file to track the last checked commit.

## How to Use

1. **Install:** `pip install pygithub python-dotenv gitpython`
2. **.env File:** Create a `.env` file with your GitHub token (`GIT_TOKEN`) and branch name (`BRANCH`).  *Do not commit this file.*
3. **Clone:** Clone the repository you want to update.
4. **Run:** Place the script in the cloned directory and run it with `python your_script_name.py`.

## Prerequisites

* Python 3.x
* GitHub account
* Cloned repository

## Key Ideas

* **Automation:**  Keeps your local repo up-to-date.
* **Security:** Protect your GitHub token.
* **Simplicity:** Easy to set up and use.