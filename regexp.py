import re
import glob
import os
from datetime import datetime
from dateutil import relativedelta

# Scratchpad
# Some python code to pick out date patterns from files in a directory, and tell the time difference between current date and the filename's date

for name in glob.glob('sample_files/*'):
  try:
    r1 = re.findall("\d{4}-\d{2}-\d{2}", name)
    first_date_match = r1[0]
    file_date_obj = datetime.strptime(first_date_match, '%Y-%m-%d')
    now = datetime.now()
    
    delta = relativedelta.relativedelta(now, file_date_obj)
    print(name + '   ' + first_date_match + str(delta.years))

  except Exception as expn:
    print(expn)
    pass
  
  
