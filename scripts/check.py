import git
import os
import sys

# Define the repository URL and the local destination path
repo_url = "https://github.com/gitpython-developers/QuickStartTutorialFiles.git"
local_dir = "./cloned_repo" # The local directory to clone into

comments = sys.argv[1].splitlines()
for comment_line in comments:
  if 'action' in comment_line:
    action = comment_line.split(':')
    if action[1] == 'test':
      print("testing")
    else:
      print("Enter a valid action")
      exit()
  elif 'source' in comment_line:
    source = comment_line.split(':')
    try:
      repo = git.Repo.clone_from('https://github.com/calebu_/' + source[1], source[1])
      print(f"Repository successfully cloned to {os.path.abspath(source[1])}")
    except Exception as clone_exc:
      print(f"Unable to clone source {source[1]}")
      exit()
  elif 'target' in comment_line:
    target = comment_line.split(':')
    try:
      repo = git.Repo.clone_from('https://github.com/calebu_/' + target[1], target[1])
      print(f"Repository successfully cloned to {os.path.abspath(target[1])}")
    except Exception as clone_exc:
      print(f"Unable to clone source {target[1]}")
      exit()
