__author__ = 'sara'
import subprocess
import os


def run():
    cmd = "python3 /Users/sara/PycharmProjects/webAutoTest/jobs/webAutoTest/run.py"
    os.popen(cmd)

    f = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).communicate()[0]

    print(f)

    print(1)


run()