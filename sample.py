#!/usr/bin/python
# Play with json module
# Writes json to an output file tester.txt

import sys, json, logging, yaml

logger = logging.getLogger(__name__)
print (len(sys.argv))
print (f"From python code: {sys.argv[1]}")

with open('main\test.yml', 'r') as file:
    config = yaml.safe_load(file)

print(config)

if len(sys.argv) > 1 and sys.argv[1] == 'check-changes':
	print("<html><body><h3>Changes to be made</h3><table><tr><td>Repo</td><td>Branch</td><td>Change</td></tr><tr><td>Repo 1</td><td>Main</td><td>++ line added</td></tr></table></body></html>")
	exit()
f = open("tester.txt", "a")
f.write("[]")
f.close()

f = open("tester.txt", "r")
content = f.read()
obj = json.loads(content)
dict = {"name" : "one"}
obj.append(dict)
dict = {"name" : "two"}
obj.append(dict)
dict = {"name" : "three"}
obj.append(dict)
dict = {"name" : "four"}
obj.append(dict)
obj = json.dumps(obj, indent = 2)
print(obj)

logger.info(f"{obj}")



