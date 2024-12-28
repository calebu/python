import sys, subprocess
import datetime
from smtplib import SMTP

debuglevel = 0

smtp = SMTP()
smtp.set_debuglevel(debuglevel)
smtp.connect('smtp.gmail.com', 587)
smtp.login('naija.techie.2018@gmail.com', 'NMRC$$2kay')

from_addr = "Caleb Adeyemi <calebadeyemi@gmail.com>"
to_addr = "naija.techie.2018@gmail.com"

subj = "hello"
date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )

message_text = "Hello\nThis is a mail from your server\n\nBye\n"

msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( from_addr, to_addr, subj, date, message_text )

files =  ' '.join(sys.argv[1:]).split(' ')
subprocess.call("docker pull ghcr.io/tmknom/dockerfiles/prettier", shell=True)
for file in files:
    res = subprocess.call(f"docker run --rm -v $(pwd):/work tmknom/prettier --check {file} --parser typescript > output.txt 2>&1", shell=True)
    str = open('output.txt', 'r').read()
    if "[warn]" in str or "[error]" in str:
        smtp.sendmail(from_addr, to_addr, msg)
        smtp.quit()
        sys.exit(f"File {file} failed the format check")
    
    
