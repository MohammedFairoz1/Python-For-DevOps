import subprocess
print("enter which environment it is")
env = input()
tag = "latest"
image = "nginx"
if env == "dev":
    port = "8080"
elif env == "stage":
    port = "8081"
else:
    port = "443"
cmd = "docker run -p " + port + ":" + port + " " + image
print(cmd)
subprocess.run(cmd, shell=True)
# subprocess.run(f"docker run -p {port}:{port} {image}", shell=True)