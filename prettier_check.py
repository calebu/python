import sys, subprocess

files =  ' '.join(sys.argv[1:]).split(' ')
subprocess.call("docker pull ghcr.io/tmknom/dockerfiles/prettier", shell=True)
for file in files:
    res = subprocess.call(f"docker run --rm -v $(pwd):/work tmknom/prettier --check {file} --parser typescript >> output1.txt 2>&1", shell=True)
subprocess.call("cat output1.txt", shell=True)