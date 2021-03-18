import subprocess
import time
print("Would you like to run FixWifi")
if str(input()) == "YES":
    subprocess.run("rfkill block wifi")
    time.sleep(3)
    subprocess.run("rfkill unblock wifi")
else:
    print("ok")