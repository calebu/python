import git
import os
import sys

comments = sys.argv[1].splitlines()
for comment_line in comments:
  if 'action' in comment_line:
    action = comment_line.split(':')
    if action[1] == 'test':
      pass
    else:
      print("Enter a valid action")
      exit()
  elif 'source' in comment_line:
    source = comment_line.split(':')
    source[1] = source[1].strip()
    try:
      repo = git.Repo.clone_from(f'https://calebu:{sys.argv[1]}@github.com/calebu/' + source[1], source[1])
      print(f"Repository successfully cloned to {os.path.abspath(source[1])}")
    except Exception as clone_exc:
      print(f"Unable to clone source repo: {clone_exc}")
      exit()
  elif 'target' in comment_line:
    target = comment_line.split(':')
    target[1] = target[1].strip()
    try:
      repo = git.Repo.clone_from(f'https://calebu:{sys.argv[1]}@github.com/calebu/' + target[1], target[1])
      print(f"Repository successfully cloned to {os.path.abspath(target[1])}")
    except Exception as clone_exc:
      print(f"Unable to clone source repo: {clone_exc}")
      exit()
