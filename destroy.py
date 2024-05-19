from deploy import get_files, sync_dir
import subprocess

def destroy():
    for path in sync_dir:
        root_files = get_files(path)
        print("Destroying {} files...".format(root_files))
        pr = subprocess.run(['rm', root_files])
        if pr.returncode != 0:
            print("Failed to remove {} files.".format(root_files))
            return False
        else:
            print("Successfully removed {} files.".format(root_files))
            return True


destroy()
