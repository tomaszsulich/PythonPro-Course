from pathlib import Path

path0 = Path() / "subdir"
path1 = path0 / "subdir2"
file0 = path1 / "file0.txt"
print(path0, path1, sep = "\n")