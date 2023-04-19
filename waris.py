import os, sys
try:
    __import__("waris").waris()
except Exception as e:
    exit(str(e))
