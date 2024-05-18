import os
import subprocess
from typing import List, Tuple

current_dir: str = os.getcwd()
sync_dir: List[str] = ["./etc/nginx"]  # dirs to symbolic link them

def get_files(path: str) -> Tuple[List[str], List[str]]:
    root_files: List[str] = []
    sync_files: List[str] = []
    for root, dirs, files in os.walk(path):
        for f in files:
            relative_path = os.path.relpath(os.path.join(root, f), start=current_dir)
            root_files.append(os.path.join(current_dir, relative_path))
            sync_files.append(relative_path)
    return root_files, sync_files

def ln_conf(file_in: str, file_out: str) -> subprocess.Popen:
    command: str = f"sudo ln {file_in} {file_out}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        print(f"sync file {file_in} -> {file_out}")
    else:
        print(f"error sync file {file_in} -> {file_out}")
        print(stderr.decode())


def deploy() -> None:
    for path in sync_dir:
        i = 0
        root_files, sync_files = get_files(path)
        for s_files in sync_files:
            print(sync_files[i], root_files[i])
            ln_conf(sync_files[i], root_files[i])
            i += 1

deploy()
