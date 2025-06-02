#!/bin/python3
import os

print(*os.popen("whoami"))

# ===============Print content of current directory===============#
#!/bin/python3
from os import popen

print(popen("ls -la"))  # выведет объект, а не результат команды
print(*popen("ls -la"))
print(popen("ls -la").read().strip())  # the same result as with *
print(*popen("sleep 3"))
print(*popen("clear"))

# ===============Print content of custom directory===============#
#!/bin/python3
import os

MY_DIR = os.path.expanduser("~/Downloads")
print(*os.popen(f"echo '{MY_DIR}'"))
print(*os.popen(f"ls -la '{MY_DIR}'"))

# ===============Print write line to a file===============#
#!/bin/python3
import os

MY_FILE = "./foo.txt"
with open(MY_FILE, "w") as mf:
    mf.write("Hello, file")
with open(MY_FILE) as cf:
    print(*cf)

# ===============Show info about a file===============#
#!/bin/python3
import os

MY_FILE = "./foo.txt"
print(*os.popen("chmod +x " + MY_FILE))
print(*os.popen("stat " + MY_FILE))  # using os.popen to execute shell's stat command
print(os.stat(MY_FILE))  # using os.stat for direct file status access
print(os.stat(MY_FILE).st_uid)  # print only the user ID (UID) of the file owner

# ===============Show current time===============#
#!/bin/python3
import time

print(time.localtime())  # Print local time
print("GMT", time.gmtime())  # Print UTC/GMT time

# ===============Show description of the command===============#
#!/bin/python3
from subprocess import Popen

cms = Popen(["whatis", "pwd"])
cms.wait()

# ===============Create directory and file, then delete them===============#
#!/bin/python3
import os, subprocess

subprocess.Popen(["mkdir", "./Downloads/test/"]).wait()
subprocess.Popen(["touch", "./Downloads/test/any_file.txt"]).wait()
print(*os.walk("./Downloads/test/"))  # show conten of the directory
subprocess.Popen(["rm", "-rf", "./Downloads/test/"]).wait()
print(*os.walk("./Downloads/"))

# ===============Find file===============#
#!/bin/python3
from subprocess import Popen


def FindByPopenFind(pattern):
    cmd = Popen(
        ["find", ".", "-type", "f", "-name", pattern]
    )  # in current directory find file with name
    code = cmd.wait
    if code == 0:
        return True
    return False


FindByPopenFind("kustomize")

# ===============Find path to the app===============#
#!/bin/python3
from subprocess import Popen


def FindByPopenWhereis(pattern):
    cmd = Popen(["whereis", pattern])
    code = cmd.wait()
    if code == 0:
        return True
    return False


FindByPopenWhereis("kubectl")

# ===============Print each command-line argument passed to it===============#
#!/bin/python3
import sys

for ss, word in enumerate(sys.argv, 1):
    print(ss, word)

print("Done!")

"""
# if run this './script.py 0 1 2' will print:
1 ./my_python.py
2 0
3 1
4 2
Done!
"""
