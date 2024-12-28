import sys, subprocess

files =  ' '.join(sys.argv[1:]).split(' ')
for file in files:
    res = subprocess.call(f"docker pull ghcr.io/tmknom/dockerfiles/prettier && docker run --rm -v $(pwd):/work tmknom/prettier --check {file} --parser typescript >> output.txt 2>&1", shell=True)
