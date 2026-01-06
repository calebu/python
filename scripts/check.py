import git
import os
import sys

# Define the repository URL and the local destination path
repo_url = "https://github.com/gitpython-developers/QuickStartTutorialFiles.git"
local_dir = "./cloned_repo" # The local directory to clone into

print(sys.argv)

# Use clone_from to clone the repository
try:
    repo = git.Repo.clone_from(repo_url, local_dir)
    print(f"Repository successfully cloned to {os.path.abspath(local_dir)}")
except git.exc.GitCommandError as e:
    print(f"Error during cloning: {e}")

