import subprocess
def restart_service(service_name):
    command = f"sudo systemctl restart {service_name}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        print(f"Service {service_name} wurde erfolgreich neu gestartet.")
    else:
        print(f"Fehler beim Neustarten des Service {service_name}:")
        print(stderr.decode())


def pull_update():
    try:
        result = subprocess.run(["git", "pull"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print(f"Pulled update to {result.stdout.decode()}")
        else:
            print(f"Failed to  pull update from {result.stderr.decode()}")
            print(result.stderr.decode())
    except subprocess.CalledProcessError as e:
        print(f"Failed to pull update from {e.stderr.decode()}")
        print(e.stderr.decode())



def update():
    pull_update()# test
    restart_service("nginx")
