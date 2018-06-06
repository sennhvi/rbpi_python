# Usage:
# python3 chapter10-system-call.py -f /proc/cpuinfo

import subprocess
from optparse import OptionParser

parser = OptionParser()  # OptionParser object
# add a option parser, add more if u need, -h for help is added as default
parser.add_option("-f", "--file", dest="filename", help="The file to display")
options, arguments = parser.parse_args()

if options.filename:
    p = subprocess.Popen(["cat", options.filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    text = p.stdout.read().decode()
    error = p.stderr.read().decode()
else:
    test = ""
    error = "Filename not given"
if len(error) > 0:
    print("*****ERROR*****")
    print(error)
else:
    print(text)
