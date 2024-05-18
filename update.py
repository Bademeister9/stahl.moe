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

restart_service("nginx")
