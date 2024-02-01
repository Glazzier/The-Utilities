import subprocess

result = subprocess.run(["pip", "freeze"], capture_output=True, text=True)
installed_packages = result.stdout.split('\n')

for package in installed_packages:
    if package:
        subprocess.run(["pip", "uninstall", "-y", package.split('=')[0]])

print("Todos los paquetes han sido desinstalados.")