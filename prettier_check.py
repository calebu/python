import sys, subprocess

files =  ' '.join(sys.argv[1:]).split(' ')
subprocess.call(f"docker pull ghcr.io/tmknom/dockerfiles/prettier")
for file in files:
    res = subprocess.call(f"docker run --rm -v $(pwd):/work tmknom/prettier --check {file} --parser typescript >> output.txt 2>&1", shell=True)
subprocess.call("cat output.txt")