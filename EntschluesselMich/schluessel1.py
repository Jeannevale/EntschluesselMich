import time
import csv
import sys
from Subfolder.Object_class import Schluessel
from Subfolder.Object_class import Antivirus

schluessel=Schluessel()

if schluessel.note=="NOE":
    try:
        raise Antivirus()
    except Antivirus as e:
        print(e.text, file=sys.stderr)
        print(e.line, file=sys.stderr)
        print(e, file=sys.stderr)
        exit()

while True:
    time.sleep(1)
    with open("file.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        riga=list(reader)[0][0]
    print(riga)