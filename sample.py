#!/usr/bin/python
# Play with json module
# Writes json to an output file tester.txt

import sys, json, logger

print (len(sys.argv))
print (f"From python code: {sys.argv[1]}")
if len(sys.argv) > 1 and sys.argv[1] == 'sample':
	print("Hi")
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

logger.info(f"{test}")
logger.info(f"{test}")
logger.info(f"{test}")

