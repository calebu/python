import sys, subprocess

files =  ' '.join(sys.argv[1:]).split(' ')
subprocess.call("docker pull ghcr.io/tmknom/dockerfiles/prettier", shell=True)
for file in files:
    res = subprocess.call(f"docker run --rm -v $(pwd):/work tmknom/prettier --check {file} --parser typescript > output.txt 2>&1", shell=True)
    str = open('output.txt', 'r').read()
#    if "[warn]" in str or "[error]" in str:
#        sys.exit(f"File {file} failed the format check")
    
    
