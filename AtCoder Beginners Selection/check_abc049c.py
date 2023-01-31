import os
import subprocess

files = os.listdir("abc049c")
for f in files:
    print(f"case {f}:")
    subprocess.run(
        f"cat abc049c/{f} | python ABC049C\ -\ 白昼夢.py", text=True, shell=True
    )
